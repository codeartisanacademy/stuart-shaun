# parent class or super class
class Product:

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def sell(self):
        print("selling the product " + self.name)

    def __str__(self):
        return self.name

# computer inherits from product
# subclass or childclass
class Computer(Product):
    
    def __init__(self, name, price, description, memory, os ):
        # super function to initialize the super class properties
        super().__init__(name, price, description)
        self.memory = memory
        self.os = os

    # method override 
    def sell(self):
        print("Selling computer product " + self.name)

# create a class for Book inhertis from Product
# create a function in the Book to calculate the price per page

hp = Computer("hp", "price", "computer from hp", 16, "Microsoft Windows")

print(hp.name)
hp.sell()