#--> DataClasses
from dataclasses import dataclass

# class MyClass:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b

#     def __add__(obj, obj1):
#         obj.a += obj1.a
#         obj.b += obj1.b
#         return obj


#     def addme(self):
#         return self.a + self.b
    
#     def greetings(self):
#         print('Hello Sakeeb...')

#     def __eq__(self,  obj1):
#         if (obj.a==obj1.a) and (obj.b==obj1.b):
#             return True
#         else:
#             return False
        
#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b})'

# obj = MyClass(30, 40)
# obj1 = MyClass(30, 40)

# print(obj.addme())
# obj.greetings()

# temp = obj + obj1
# print(temp.a, temp.b)

# print(obj==obj1)

# print(obj)

#-----------------------
# __init__, __repr__, __eq__
# @dataclass
# class MyDataClass:
#     a : int=0
#     b : int=0

#     def __add__(obj, obj1):
#         obj.a += obj1.a
#         obj.b += obj1.b
#         return obj.a, obj.b
    
#     def addme(self):
#         return sum([self.a, self.b])

#     def greetings(self):
#         print('Hello Sakeeb...')

# obj = MyDataClass(10, 20)
# obj2 = MyDataClass(10, 20)

# print(obj.addme())
# obj.greetings()

# print(obj + obj2)

# print(obj==obj2)

# print(obj)

#----------------------------------------------------



dic = {'eno':100, 'ename':'sakeeb', 'esal':10000.0}

import json
jsondata = json.dumps(dic)
print(jsondata)

@dataclass(kw_only=True)
class Employee:
    eno:int
    ename:str
    esal:float

# obj = Employee(*list(dic.values()))
obj = Employee(dic)
print(obj.__dict__)