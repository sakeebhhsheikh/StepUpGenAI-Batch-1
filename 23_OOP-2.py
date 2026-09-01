#--> Inheritance

#1. Single Inheritance
#2.  Multi-level

class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()

#--------------------------
#Example : 

# class Vehicle:
#     def start(self):
#         print('Vehicle Started...')

# class Car(Vehicle):
#     def drive(self):
#         print('Driving Car...')

# class SportsCar(Car):
#     def turbo(self):
#         print('Turbo mode ON.')

# obj = SportsCar()
# obj.start()
# obj.drive()
# obj.turbo()

#----------------------------------------
#--> Hierarchical Inheritance

# class Employee:
#     a=10

# class Developer(Employee):
#     b=20

# class Tester(Employee):
#     c=30

# dobj = Developer()
# print(dobj.a, dobj.b)


# tobj = Tester()
# print(tobj.a, tobj.c)

#---------------------------------------
#-->  Hybrid

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# ---------------------------------------

#Method Overriding and using super()

# class Animal:
#     def sound(self):
#         print('Animal Sound')

# class Dog(Animal):
#     def sound(self):
#         print('Bark')
# obj = Dog()
# obj.sound()


#--> Using super() to for Parent class Constructor

#Example : 

# class Employee:
#     def __init__(self, name):
#         self.name = name
#         print('Employee Constructor...')
# # eobj = Employee('Sakeeb')

# class Developer(Employee):
#     def __init__(self, name, language):
#         print('Developer Constructor')
#         super().__init__(name)
#         self.language = language

# obj = Developer('Sakeeb', 'Python')
# print(obj.name, obj.language)

#Example : Multiple Inheritance with super()
# class A:
#     def __init__(self):
#         self.a=10
#         print('Class A')

# class B:
#     def __init__(self):
#         self.b=20
#         print('Class B')

# class C(A, B):
#     def __init__(self):
#         self.c=30
#         super().__init__()
#         print('Class C')

# obj = C()

# #Method Resolution Order(MRO)
# print(C.mro())

#------------------------------------------------

#Example : Factory Design pattern
# from math import pi

# class Circle:
#     def __init__(self, radius):
#         print('Circle Constructor...')
#         self.type = 'Circle'
#         self.radius = radius

#     def area(self):
#         print(f'Area of {self.type} : {pi * self.radius**2}')

# class Rectangle:
#     def __init__(self, l, b):
#         print('Rectangle Constructor...')
#         self.type = 'Rectangle'
#         self.l = l
#         self.b = b

#     def area(self):
#         print(f'Area of {self.type} : {(1/2)*(self.l)*(self.b)}')


# class Shape:
#     def __init__(self, *args):
#         if args[0].lower() == 'circle':
#             self.obj = Circle(args[1])
#         elif args[0].lower().startswith('rect'):
#             self.obj = Rectangle(args[1], args[2])
#         else:
#             print('Invalid Shape Type.....')
    
#     def area(self):
#         self.obj.area()

# shapeobj = Shape('circle', 10)
# shapeobj.area()
# shapeobj = Shape('rectangle', 10, 5)
# shapeobj.area()

#----------------------------------------------------------------------------

# from math import pi
# from abc import ABC, abstractmethod

# class Interface(ABC):
#     @abstractmethod
#     def area(self): 
#         pass


# class Circle(Interface):
#     def __init__(self, radius):
#         print('Circle Constructor...')
#         self.type = 'Circle'
#         self.radius = radius

#     def area(self):
#         print(f'Area of {self.type} : {pi * self.radius**2}')

# class Rectangle(Interface):
#     def __init__(self, l, b):
#         print('Rectangle Constructor...')
#         self.type = 'Rectangle'
#         self.l = l
#         self.b = b

#     def area(self):
#         print(f'Area of {self.type} : {(1/2)*(self.l)*(self.b)}')

# class Shape:
#     def __init__(self, *args):
#         if args[0].lower() == 'circle':
#             self.obj = Circle(args[1])
#         elif args[0].lower().startswith('rect'):
#             self.obj = Rectangle(args[1], args[2])
#         else:
#             print('Invalid Shape Type.....')
    
#     def area(self):
#         self.obj.area()

# shapeobj = Shape('circle', 10)
# # shapeobj.area()
# shapeobj = Shape('rectangle', 10, 5)
# # shapeobj.area()

#==========================================================

#-> Property Decorator
#-> dundar method / Magic methods

#------------------------------------------

#-> Property Decorator

#==> Example : 
# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def area(self):
#         return pi * self.__radius**2
    
#     @property
#     def radius(self):
#         return self.__radius

#     @radius.setter
#     def radius(self, radius):
#         self.__radius = radius
    
#     @radius.deleter
#     def radius(self):
#         del self.__radius

# obj = Circle(10)
# # print(obj.area())
# print(obj.area)
# print(obj.radius)

# obj.radius = 20
# print(obj.radius)

# del obj.radius
#---------------------------------------------

# (basic, hra, da, ta)
# class Employee:
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.basic = esal[0]
#         self.hra = esal[1]
#         self.da = esal[2]
#         self.ta = esal[3]

#     @property
#     def esal(self):
#         return self.basic + self.hra + self.da + self.ta
    
#     @esal.setter
#     def esal(self, tup):
#         self.basic = tup[0]
#         self.hra = tup[1]
#         self.da = tup[2]
#         self.ta = tup[3]

#     @esal.deleter
#     def esal(self):
#         del self.basic
#         del self.hra
#         del self.da
#         del self.ta
    
# obj = Employee(100, 'sakeeb', (10,20,30,40))
# print(obj.esal)

# obj.esal = (20,30,40,50)
# print(obj.esal)

#=====================================================
#==> Dundar methods
# __init__
# __new__
# __str__
# __repr__
# __eq__
# __lt__
# __gt__
# __len__
# __entry__
# __exit__
# __iter__
# __next__
# __add__

#==> Example : 
# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies

#     def __str__(self):
#         return f"Title:{self.title}, Copies:{self.copies}"
    
#     def __len__(self):
#         return len(self.title)
    
#     def __gt__(self, obj):
#         if self.copies>obj.copies:
#             return True
#         else:
#             return False

# obj1 = Book('Jungle Book', 100)
# obj2 = Book('Cyber Secutiry with AI', 50)
# print(obj1)
# print(len(obj1))

# if obj1>obj2:
#     print('obj1 have more copies than obj2')

# string = 'This is my first line\nThis is my second line'
# print(string)
# print(repr(string))
#----------------------------------------------------
#==> Operator Overloading
# 10 < 20
# 'abc' < 'xyz'

# print(10<20)
# print('ax'<'aa')

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return f'a:{self.a} b:{self.b}'
#     def __add__(self, secondobj):
#         return MyClass(self.a+secondobj.a, self.b+secondobj.b)

# obj1 = MyClass(10,20)
# obj2 = MyClass(20,30)
# print(obj1)
# print(obj2)
# print(obj1 + obj2)

#-------------------------------------------------------

# class MyClass:
#     def __new__(cls):
#         print('__new__ executed...')

#     def __init__(self):
#         print('constructor executed...')

    
# obj = MyClass()
# print(obj)

# print(type(obj))
# print(type(MyClass))

#------------------------------------------
#-> Metaclass type

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b 
    
#     def addme(self):
#         print(self.a+self.b)

# obj = MyClass(10,20)
# obj.addme()


# def addme(self):
#     print(self.a+self.b)

# MyClass = type('MyClass', (), {'a':10,'b':20, 'addme':addme})

# obj = MyClass()
# obj.addme()

#--------------------------------------------------------------------
#-> Context Manager
#-> Iterators

#-----------------------
#==>  Context Manager
# __enter__
# __exit__

# class ContextManager:
#     def __init__(self, val):
#         print('Constructor Executed...')
#         self.val = val

#     def __enter__(self):
#         print('Enter Executed...')
#         return self
    
#     def __exit__(self, a, b, c):
#         print('Exit Executed...')

# obj = ContextManager(20)
# print(obj.val)

# with ContextManager(10) as obj:
#     input(obj.val)
#     raise ValueError('Test Error')

#--------------------------------------------

# class LoginManager:
#     def __init__(self, usrname, passwd):
#         self.usrname = usrname
#         self.passwd = passwd
#         self.loginstatus = False

#     def __login(self):
#         self.loginstatus = True
#         print(f'Using {self.usrname} and {self.passwd} we have loggedin...')
#         return 'connected'

#     def __logout(self):
#         self.loginstatus = False
#         print('Logged out successfully...')

#     def __enter__(self):
#         self.__login()
#         return self.loginstatus
    
#     def __exit__(self, exc_val, exc_type, exc_tb):
#         self.__logout()


# with LoginManager('abc','xyz@123') as loginstatus:
#     print(loginstatus)
#     print('Perform some queries...')



# fobj = open('myfile.txt', 'w')
# fobj.write('this is my line in file.')
# fobj.close()

# with open('myfile.txt', 'w') as fobj:
#     fobj.write('this is my line in file.')
from datetime import datetime

class FileReaderWriter:
    def __init__(self, fname, fmode):
        self.fname = fname
        self.fmode = fmode
        self.file = None
        self.logfile = 'activity_log.csv'

    def __enter__(self):
        self.file = open(self.fname, self.fmode)
        record = f'file Open,{self.fname},{self.fmode},{datetime.now().strftime('%Y-%m-%d %H:%M')}\n'
        with open(self.logfile, 'a') as fobj:
            fobj.write(record)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        record = f'file Close,{self.fname},{self.fmode},{datetime.now().strftime('%Y-%m-%d %H:%M')}\n'
        with open(self.logfile, 'a') as fobj:
            fobj.write(record)
        self.file.close()

with FileReaderWriter('myfile.txt', 'w') as fobj:
    fobj.write('this is my line in file.')

# itertool
# dataclasses