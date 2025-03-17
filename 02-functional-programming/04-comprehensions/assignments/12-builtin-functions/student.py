import re

class Movie:
    def __init__(self, title, runtime, director, actors, year, genres):
        self.title = title
        self.runtime = runtime
        self.director = director
        self.actors = actors
        self.year = year
        self.genres = genres



movies = [
    Movie(
        title="Magnolia",
        year=1999,
        runtime=188,
        director='Paul Thomas Anderson',
        actors=[
            'Tom Cruise',
            'Jason Robards',
            'Philip Seymour Hoffman',
            'Julianne Moore',
            'Philip Baker Hall',
            'John C. Reilly',
            'Alfred Molina',
            'William H. Macy',
        ],
        genres=['Drama'],
    ),
    Movie(
        title='Once Upon a Time in the West',
        year=1968,
        runtime=165,
        director='Sergio Leone',
        actors=['Henry Fonda', 'Charles Bronson', 'Jason Robards'],
        genres=['Western'],
    ),
    Movie(
        title='Requiem for a Dream',
        year=2000,
        runtime=102,
        director='Darren Aronofsky',
        actors=['Jared Leto', 'Marlon Wayans', 'Ellen Burstyn', 'Jennifer Connelly'],
        genres=['Drama'],
    ),
    Movie(
        title='True Romance',
        year=1993,
        runtime=119,
        director='Tony Scott',
        actors=['Christian Slater', 'Dennis Hopper', 'Val Kilmer', 'Patricia Arquette', 'Christopher Walken', 'James Gandolfini', 'Brad Pitt', 'Gary Oldman', 'Samuel L. Jackson'],
        genres=['Crime', 'Drama', 'Romance'],
    ),
    Movie(
        title='Oldboy',
        year=2003,
        runtime=120,
        director='Park Chan-wook',
        actors=['Choi Min-sik', 'Yoo Ji-tae', 'Kim Byeong-Ok'],
        genres=['Action', 'Drama', 'Mystery'],
    ),
    Movie(
        title='Lady Vengeance',
        year=2005,
        runtime=115,
        director='Park Chan-wook',
        actors=['Nam-mi Kang', 'Jeong-nam Choi', 'Hye-Sook Go', 'Bok-hwa Baek'],
        genres=['Crime', 'Drama', 'Thriller'],
    ),
    Movie(
        title='The Handmaiden',
        year=2016,
        runtime=145,
        director='Park Chan-wook',
        actors=['Ha Jung-woo', 'Cho Jin-woong'],
        genres=['Drama', 'Romance', 'Thriller'],
    ),
    Movie(
        title='The Master',
        year=2012,
        runtime=138,
        director='Paul Thomas Anderson',
        actors=['Joaquin Phoenix', 'Philip Seymour Hoffman', 'Jesse Plemons', 'Amy Adams'],
        genres=['Drama'],
    ),
    Movie(
        title='Phantom Thread',
        year=2017,
        runtime=130,
        director='Paul Thomas Anderson',
        actors=['Vicky Krieps', 'Daniel Day-Lewis', 'Lesley Manville', 'Julie Vollono'],
        genres=['Drama', 'Romance'],
    ),
    Movie(
        title='There Will Be Blood',
        year=2007,
        runtime=158,
        director='Paul Thomas Anderson',
        actors=['Daniel Day-Lewis', 'Paul Dano', 'Ciaran Hinds', 'Martin Stringer'],
        genres=['Drama'],
    ),
    Movie(
        title='The Good, the Bad and the Ugly',
        year=1966,
        runtime=161,
        director='Sergio Leone',
        actors=['Clint Eastwood', 'Eli Wallach', 'Lee Van Cleef'],
        genres=['Adventure', 'Western'],
    ),
    Movie(
        title='A Fistful of Dollars',
        year=1964,
        runtime=99,
        director='Sergio Leone',
        actors=['Clint Eastwood'],
        genres=['Action', 'Drama', 'Western'],
    ),
    Movie(
        title='For a Few Dollars More',
        year=1965,
        runtime=132,
        director='Sergio Leone',
        actors=['Clint Eastwood', 'Lee Van Cleef'],
        genres=['Western'],
    ),
    Movie(
        title='Black Swan',
        year=2010,
        runtime=108,
        director='Darren Aronofsky',
        actors=['Vincent Cassel', 'Natalie Portman', 'Mila Kunis', 'Winona Ryder'],
        genres=['Drama', 'Thriller'],
    ),
    Movie(
        title='Blade Runner',
        year=1982,
        runtime=117,
        director='Ridley Scott',
        actors=['Harrison Ford', 'Rutger Hauer', 'Edward James Olmos'],
        genres=['Action', 'Drama', 'Sci-Fi'],
    ),
    Movie(
        title='Blade Runner 2049',
        year=2017,
        runtime=164,
        director='Denis Villeneuve',
        actors=['Harrison Ford', 'Ryan Gosling', 'Ana de Armas', 'Dave Bautista'],
        genres=['Action', 'Drama', 'Mystery', 'Sci-Fi'],
    ),
    Movie(
        title="Miller's Crossing",
        year=1990,
        runtime=115,
        director='Coen Brothers',
        actors=['Gabriel Byrne', 'Albert Finney', 'John Turturro', 'Marcia Gay Harden'],
        genres=['Crime', 'Drama', 'Thriller'],
    ),
   Movie(
        title='No Country for Old Men',
        year=2007,
        runtime=122,
        director='Coen Brothers',
        actors=['Tommy Lee Jones', 'Javier Bardem', 'Josh Brolin', 'Woody Harrelson'],
        genres=['Crime', 'Drama', 'Thriller'],
    ),
    Movie(
        title='True Grit',
        year=2010,
        runtime=110,
        director='Coen Brothers',
        actors=['Jeff Bridges', 'Matt Damon', 'Josh Brolin', 'Hailee Steinfeld'],
        genres=['Drama', 'Western'],
    ),
    Movie(
        title='Fargo',
        year=1996,
        runtime=98,
        director='Coen Brothers',
        actors=['Steve Buscemi', 'Peter Stormare', 'William H. Macy', 'Frances McDormand'],
        genres=['Crime', 'Thriller'],
    ),
    Movie(
        title='The Big Lebowski',
        year=1998,
        runtime=117,
        director='Coen Brothers',
        actors=['Jeff Bridges', 'John Goodman', 'Steve Buscemi', 'Philip Seymour Hoffman', 'Julianna Moore'],
        genres=['Comedy', 'Crime'],
    ),
    Movie(
        title='The Martian',
        year=2015,
        runtime=144,
        director='Ridley Scott',
        actors=['Matt Damon', 'Sean Bean', 'Jessica Chastain', 'Kristen Wiig', 'Kate Mara'],
        genres=['Adventure', 'Drama', 'Sci-Fi'],
    ),
    Movie(
        title='Stranger Than Fiction',
        year=2006,
        runtime=113,
        director='Marc Forster',
        actors=['Will Ferrell', 'Dustin Hoffman', 'Emma Thompson', 'Maggie Gyllenhaal'],
        genres=['Comedy', 'Drama', 'Fantasy'],
    ),
    Movie(
        title='Batman Begins',
        year=2005,
        runtime=140,
        director='Christopher Nolan',
        actors=['Christian Bale', 'Michael Caine', 'Ken Watanabe', 'Liam Neeson', 'Gary Oldman', 'Cillian Murphy'],
        genres=['Action', 'Crime', 'Drama'],
    ),
    Movie(
        title='The Dark Knight',
        year=2008,
        runtime=152,
        director='Christopher Nolan',
        actors=['Christian Bale', 'Heath Ledger', 'Aaron Eckhart', 'Michael Caine', 'Gary Oldman', 'Cillian Murphy', 'Maggie Gyllenhaal'],
        genres=['Action', 'Crime', 'Drama'],
    ),
    Movie(
        title='The Dark Knight Rises',
        year=2012,
        runtime=164,
        director='Christopher Nolan',
        actors=['Christian Bale', 'Tom Hardy', 'Gary Oldman', 'Michael Caine', 'Cillian Murphy'],
        genres=['Action', 'Thriller', 'Drama'],
    ),
    Movie(
        title='The Prestige',
        year=2006,
        runtime=130,
        director='Christopher Nolan',
        actors=['Christian Bale', 'Hugh Jackman', 'Michael Caine', 'Scarlett Johansson'],
        genres=['Drama', 'Mystery', 'Sci-Fi'],
    ),
    Movie(
        title='Inception',
        year=2010,
        runtime=148,
        director='Christopher Nolan',
        actors=['Tom Hardy', 'Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page', 'Ken Watanabe', 'Cillian Murphy'],
        genres=['Action', 'Adventure', 'Sci-Fi'],
    ),
    Movie(
        title='Interstellar',
        year=2014,
        runtime=169,
        director='Christopher Nolan',
        actors=['Matthew McConaughey', 'Ellen Burstyn', 'Casey Affleck', 'Michael Caine', 'Anne Hathaway', 'Jessica Chastain', 'John Lithgow'],
        genres=['Adventure', 'Drama', 'Sci-Fi'],
    ),
        Movie(
        title='Arrival',
        year=2016,
        runtime=116,
        director='Denis Villeneuve',
        actors=['Jeremy Renner', 'Forest Whitaker', 'Amy Adams'],
        genres=['Drama', 'Mystery', 'Sci-Fi'],
    ),
    Movie(
        title='Prisoners',
        year=2013,
        runtime=153,
        director='Denis Villeneuve',
        actors=['Hugh Jackman', 'Jake Gyllenhaal', 'Viola Davis', 'Melissa Leo', 'Paul Dano'],
        genres=['Crime', 'Drama', 'Mystery'],
    ),
    Movie(
        title='In Bruges',
        year=2008,
        runtime=107,
        director='Martin McDonagh',
        actors=['Colin Farrell', 'Brendan Gleeson', 'Ciaran Hinds'],
        genres=['Comedy', 'Crime', 'Drama'],
    ),
    Movie(
        title='Seven Psychopaths',
        year=2012,
        runtime=110,
        director='Martin McDonagh',
        actors=['Colin Farrell', 'Woody Harrelson', 'Sam Rockwell', 'Christopher Walken'],
        genres=['Comedy', 'Crime'],
    ),
    Movie(
        title='Three Billboards Outside Ebbing, Missouri',
        year=2017,
        runtime=115,
        director='Martin McDonagh',
        actors=['Frances McDormand', 'Woody Harrelson', 'Sam Rockwell', 'Caleb Landry Jones'],
        genres=['Comedy', 'Crime', 'Drama'],
    ),
    Movie(
        title='Unforgiven',
        year=1992,
        runtime=130,
        director='Clint Eastwood',
        actors=['Clint Eastwood', 'Morgan Freeman', 'Gene Hackman', 'Richard Harris'],
        genres=['Western', 'Drama'],

    ),
    Movie(
        title='Moonrise Kingdom',
        year=2012,
        runtime=94,
        director='Wes Anderson',
        actors=['Jared Gilman', 'Frances McDormand', 'Bruce Willis', 'Bill Murray', 'Tilda Swinton', 'Edward Norton'],
        genres=['Comedy', 'Drama', 'Family'],
    ),
    Movie(
        title='The Grand Budapest Hotel',
        year=2014,
        runtime=99,
        director='Wes Anderson',
        actors=['Ralph Fiennes', 'F. Murray Abraham', 'Mathieu Amalric', 'Adrien Brody', 'Willem Dafoe', 'Jeff Goldblum', 'Jude Law', 'Harvey Keitel', 'Edward Norton', 'Bill Murray', 'Saoirse Ronan', 'Tilda Swinton', 'Owen Wilson'],
        genres=['Comedy', 'Drama', 'Adventure'],

    ),
    Movie(
        title='Heat',
        year=1995,
        runtime=170,
        director='Michael Mann',
        actors=['Al Pacino', 'Robert De Niro', 'Val Kilmer', 'Jon Voight', 'Amy Brenneman', 'William Fichtner', 'Natalie Portman'],
        genres=['Action', 'Crime', 'Drama'],
    ),
    Movie(
        title='Goodfellas',
        year=1990,
        runtime=145,
        director='Martin Scorsese',
        actors=['Robert De Niro', 'Ray Liotta', 'Joe Pesci', 'Lorraine Bracco'],
        genres=['Biography', 'Crime', 'Drama'],
    ),
    Movie(
        title='Casino',
        year=1995,
        runtime=178,
        director='Martin Scorsese',
        actors=['Robert De Niro', 'Sharon Stone', 'Joe Pesci', 'James Woods', 'Don Rickles', 'Kevin Pollack'],
        genres=['Crime', 'Drama'],
    ),
    Movie(
        title='The Wolf of Wall Street',
        year=2013,
        runtime=180,
        director='Martin Scorsese',
        actors=['Leonardo DiCaprio', 'Jonah Hill', 'Margot Robbie', 'Matthew McConaughey'],
        genres=['Biography', 'Comedy', 'Crime'],
    ),
]

def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return genre in {gen for movie in movies for gen in movie.genres if movie.director == director}

def is_prime(n):
    return 2 == len([number for number in range(1, n + 1) if n % number == 0])

def is_increasing(ns):
    return all([ns[i] <= ns[i + 1] for i in range(len(ns) - 1)])

def count_matching(xs, ys):
    return sum([xs[i] == ys[i] for i in range(min(len(xs), len(ys)))])

def weighted_sum(ns, weights):
    return sum([mult[0] * mult[1] for mult in zip(ns, weights)])

def alternating_caps(string):
    return ''.join(letter.upper() if i % 2 == 0 else letter.lower() for i, letter in enumerate(string))

def find_repeated_words(sentence):
    words = sentence.lower().split()
    return {words[i] for i in range(1, len(words)) if words[i] == words[i - 1].strip(".,!?;:")}

print(movie_count(movies, "Martin Scorsese"))
print(longest_movie_runtime_with_actor(movies, "Leonardo DiCaprio"))
print(has_director_made_genre(movies, "Martin Scorsese", "Comedy"))
print(is_prime(18))
print(is_increasing([1, 3, 2, 3, 4, 5, 5]))
print(count_matching([1, 2, 1], [3, 2, 1]))
print(weighted_sum([1, 2, 3], [4, 5, 6]))
print(alternating_caps("astrology"))
print(find_repeated_words("This sentence has has repeated words. Words."))