# create a function that do something
def say_hello():
    print("hello")

say_hello()

# create a function with parameters
def greet(name):
    print("Hello " + name)

greet("john")

# create a function name add, to add 2 numbers as parameters
def add(x,y):
    print(x+y)

add(2,4)

# create a function name division, to divide 2 numbers from parameters
def divide(x,y):
    print(x/y)

divide(4,2)

# function that returns something
def subtract(x,y):
    return x-y

result = subtract(4,2)

print(result)