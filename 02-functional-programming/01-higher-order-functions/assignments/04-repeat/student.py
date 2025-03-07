def say_hello():
    print("Hello!")

def repeat(function, n):
    for i in range(n):
        function()

repeat(say_hello, 5)