#User Defined Exception

# print(dir(__builtins__))

class InvalidPassword(Exception):
    def __init__(self, msg):
        self.msg = msg

# raise InvalidPassword('This is a Test Error Message.')


acno = 123
passwd = 'abc123'

try:
    password = input('Enter your password')
    if passwd==password:
        print('Hello welcome...')
    else:
        print('Incorrect Password! You are an invalid user...')
        raise InvalidPassword('Invalid Password!')
except InvalidPassword as err:
    print('Error Occured...', err)
