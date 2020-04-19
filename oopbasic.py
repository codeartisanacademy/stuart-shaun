class SmartPhone:
    # __init__ is a function that being executed when you create an object using this class
    # this will initialize (generate) the information for the object
    # self is the first parameter for a function inside a class, self is the object itself
    def __init__(self, name, version, os, color, price):
        # properties, information about the object
        self.name = name
        self.version = version
        self.os = os
        self.color = color
        self.price = price
    
    def call(self, destination):
        print('calling {0}...'.format(destination))
    
    # create a function to send message to someone. Print "Sending message 'Hello how are you' to John"


iphone_11 = SmartPhone('iPhone 11', '11', 'iOS', 'white', 13000000)

print(iphone_11.name)

print(iphone_11.price)

print("For sale {0} color {1} at the price of {2} ".format(iphone_11.name, iphone_11.color, iphone_11.price))

iphone_11.call('John')