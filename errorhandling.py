number_input = input("Enter a number: ")

# try the execution inside the try
try:
    x = int(number_input)
    print(x*10)
# if there is an error, it goes to except
except Exception as error:
    print("There is an error. Please try again")
# finally block is always going to be executed
finally:
    print("finally block")


print("process ended")