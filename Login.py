import time


username = 'password'

password = 'password'

login_username = input('Enter Your Username: ')
login_password = input('Enter Your Password: ')

if login_password == username:
   print('You Logged Into username')
else:
    print('Login Failed')
    if login_password == password:
        print('You Logged in')
    else:
        print('Error! Try Again')
