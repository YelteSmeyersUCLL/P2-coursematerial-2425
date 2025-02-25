class Queue:
    def __init__(self):
        self.__items = []
    
    @property
    def items(self):
        return self.__items

    def add(self, item):
        self.__items.append(item)
    
    def next(self):
        return self.__items.pop(0)
    
    def is_empty(self):
        return len(self.__items) == 0

# Create an empty queue
queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

print(queue.next())   # Alice arrived first, so she's the first to be served next
print(queue.next())   # This must return Bob
print(queue.next())

