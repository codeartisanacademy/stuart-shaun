email = "john@gmail.com"

print(email)


first_name = "john"
last_name = "doe"

# combine or concatinate two strings or more using +
print(first_name + " " + last_name)

# hello Mr. john doe
print("hello mr." + first_name + " " + last_name)

# another way to join strings is using format()
# {0} and {1} is indexed placeholders

print("hello mr. {0} {1}, how are you today".format(first_name, last_name))

print("Good afternoon mr {0} {1}".format(first_name.title(), last_name.title()))

# len() is a built in function that counts how many characters in a string
print(len(first_name))

print(len("this is a string"))
