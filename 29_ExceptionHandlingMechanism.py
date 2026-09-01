#SyntaxError : Incorrect Code
#LogicalError : Invalid Code
#RuntimeError ( Exception ) : Invalid Data

# li = [1,4,2,3,6,5]
# li.sort(reverse=True)
# print(li)


# a = int(input('Enter you value:'))
# print(f'Your entered value is {a}')

#=> try, except, else, finally

# try -> Contains the actual program code to be tested for errors.
# except -> Executes whenever there is an error in try block.
# else (Optional) -> Executes when there is no error occured in try block.
# finally (Optional) -> Always Executes

try:
    pass
except:
    pass
#-----------------
try:
    pass
except:
    pass
else:
    pass
#-----------------
try:
    pass
except ValueError as e:
    pass
except TypeError as e:
    pass
except NameError as e:
    pass
except FileExistsError as e:
    pass
#-----------------
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
#-----------------
try:
    pass
finally:
    pass
#-----------------

#Example-1 : 
# try:
#     a=eval(input('Enter a value:'))
#     b=eval(input('Enter a value:'))
#     print(a+b)
# except Exception as err:
#     print(err) 

#Example-2

# a=eval(input('Enter a value:'))
# b=eval(input('Enter a value:'))
# print(a/b)

#NameError: name 'a' is not defined
#TypeError: unsupported operand type(s) for /: 'str' and 'str'
#ZeroDivisionError: division by zero

# try:
#     a=eval(input('Enter a value:'))
#     b=eval(input('Enter a value:'))
#     print(a/b)
# except NameError as err:
#     print(f'NameError : {err}')
# except TypeError as err:
#     print(f'TypeError : {err}')
# except ZeroDivisionError as err:
#     print(f'ZeroDivisionError : {err}')
# except Exception as err:
#     print(err)

# print('This is statement outside try...')

#----------------------------------------------------
# try:
#     a=eval(input('Enter a value:'))
#     b=eval(input('Enter a value:'))
#     print(a/b)
# except NameError as err:
#     print(f'NameError : {err}')
# except TypeError as err:
#     print(f'TypeError : {err}')
# except ZeroDivisionError as err:
#     print(f'ZeroDivisionError : {err}')
# except Exception as err:
#     print(err)
# else:
#     print('data loaded successfully...')
# finally:
#     print('This code always executes...')
# print('This is statement outside try...')


#Example-3
# try:
#     a=eval(input('Enter a value:'))
#     b=eval(input('Enter a value:'))
#     print(a/b)   
# finally:
#     print('This code always executes...')

# print('Statement outside try....')

#Example-4
# try:
#     try:
#         a=eval(input('Enter value of a:'))
#     except Exception as err:
#         print('Error Occured...')
#     b=eval(input('Enter value of b:'))
#     print(a/b)   
# finally:
#     print('This code always executes...')

# print('Statement outside try....')

#----------------------------------------------------------
#WAP to make the try code to execute atleast 3 times if there is error in try block, if no error it stop
# for i in range(3):
#     try:
#         a=eval(input('Enter a value:'))
#         b=eval(input('Enter a value:'))
#         print(a+b)
#     except Exception as err:
#         print(err)
#     else:
#         break
# else:
#     print('Invalid data input. program tried 3 times and stopped...')

















