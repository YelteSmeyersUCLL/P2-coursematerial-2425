def sort_by_age(people):
    return sorted(people, key=lambda person: person.age)

def sort_by_decreasing_age(people):
    lst = sorted(people, key=lambda person: person.age, reverse=True)
    return lst

def sort_by_name(people):
    return sorted(people, key=lambda person: person.name)

def sort_by_name_then_age(people):
    return sorted(people, key=lambda person: (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name}, {self.age}"
    
    def __lt__(self, other):
        return self.name < other.name
    
people = [
    Person("Alice", 30),
    Person("Alice", 25),
    Person("Bob", 25),
    Person("Bob", 35),
    Person("Charlie", 35),
    Person("Charlie", 33),
    Person("David", 20),
    Person("David", 29),
    Person("Eve", 28),
    Person("Eve", 22),
    Person("Frank", 33),
    Person("Frank", 27),
    Person("Grace", 27),
    Person("Grace", 26),
    Person("Hank", 40),
    Person("Hank", 30),
    Person("Ivy", 22),
    Person("Ivy", 24),
    Person("Jack", 29),
    Person("Jack", 31),
    Person("Kara", 26),
    Person("Kara", 35),
    Person("Leo", 31),
    Person("Leo", 23),
    Person("Mia", 24),
    Person("Mia", 21),
    Person("Nina", 38),
    Person("Nina", 30),
    Person("Oscar", 21),
    Person("Oscar", 36),
    Person("Paul", 36),
    Person("Paul", 32),
    Person("Quinn", 23),
    Person("Quinn", 28),
    Person("Rachel", 32),
    Person("Rachel", 25),
    Person("Steve", 34),
    Person("Steve", 29),
    Person("Tina", 37),
    Person("Tina", 20)
]



# print(sort_by_age(people))
# print(sort_by_decreasing_age(people))
# print(sort_by_name(people))
# print(sort_by_name_then_age(people))
print(sort_by_name_then_decreasing_age(people))