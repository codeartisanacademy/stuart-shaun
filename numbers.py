# ask user to enter a number save it to variable x
x = input('enter the first number: ')
# ask user to enter a number save it to variable y
y = input('enter the second number: ')

# ask user to enter the operation +, -, *, /
operation = input("enter +, -, *, /: ")

# convert from string to integer / number
x_int = int(x)
y_int = int(y)

# do the math operation based on the operation that user entered
if operation == '+':
    print('x + y is {0}'.format(x_int + y_int))
elif operation == '-':
    print('x - y is {0}'.format(x_int - y_int))
elif operation == '*':
    print('x * y is {0}'.format(x_int * y_int))
elif operation == '/':
    print('x / y is {0}'.format(x_int / y_int))
else:
    print("we don't know what you want.")

