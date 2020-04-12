import random

secret_number = random.randint(0,10)

# ask user to enter a number
x = input('enter a number between 1 - 10: ')
x_int = int(x)
# check if the number is equal with the secret_number
if x_int == secret_number:
    print('correct')
# if yes, you say "Correct"
else:
    print('not correct, the number is {0}'.format(secret_number))
# if not, you say, incorrect, the number is ...