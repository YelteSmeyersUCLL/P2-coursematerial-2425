import pytest
from book import *

@pytest.mark.parametrize('title, isbn', [
    ("The Hobbit", "978-0-261-10221-7"),                    # Standard book, multi-part ISBN
    ("Poems", "978-1779501127"),                         # Short title, typical ISBN
    ("A Song of Ice and Fire: A Game of Thrones", "978-055310354-0"),  # Long title, shorter ISBN
    ("Dune", "978-044117271-9"),                            # Classic book, standard ISBN
    ("Math 101", "978-3-16-148410-0")
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize('title, isbn', [
    ("", "978-0-261-10221-7"),
    ("", "978-1779501127")
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)

@pytest.mark.parametrize('title, isbn', [
    ("The Hobbit", "978-0-261-10221-790"),
    ("Poems", "978-17795011270"),
    ("A Song of Ice and Fire: A Game of Thrones", "978-055310354"),
    ("Dune", "978-044117271-90"),
    ("Math 101", "978-3-16-148410-1")
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)