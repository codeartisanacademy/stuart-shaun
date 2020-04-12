# ask user to enter email address
email = input('Enter your email address: ')

# check if the email has @, if yes print 'your email is valid', else print 'enter the correct email'
if email.count('@') > 0:
    # if the email has . after the sign john.doe@gmail.com
    at_position = email.index('@')
    dot_position = email.index('.', at_position)
    print(dot_position)
    if email.count('.') > 0:
        print('email is valid')
    else:
        print('error')
else:
    print('Enter the correct email')