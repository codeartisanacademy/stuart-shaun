import random

secret_number = random.randint(0,10)
print(secret_number)
# ask user to enter a number
x = input('enter a number between 1 - 10: ')

try:
    x_int = int(x)
    while x_int is not secret_number:
        x = input('enter a number between 1 - 10: ')
        x_int = int(x)
    
    print("Correct")
except Exception as error:
    print(error)
    

# if not, you say, incorrect, the number is ...

# modify or improve to use try execption whenever you need it