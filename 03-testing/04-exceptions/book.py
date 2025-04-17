class Book:
    def __init__(self, title, isbn):
        if not title:
            raise RuntimeError
        self.isbn = isbn
        self.title = title
    
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        xs = value.replace(" ", "-").split("-")
        digits = []
        total = 0
        for items in xs:
            for num in items:
                digits.append(int(num))
        if len(digits) != 13:
            raise RuntimeError
        for i in range(len(digits)):
            if i % 2 != 0:
                digits[i] = digits[i] * 3
            total += int(digits[i])
        if total % 10 == 0:
            self.__isbn = value
        else:
            raise RuntimeError
    
    def __repr__(self):
        return f"{self.title}, {self.isbn}"
