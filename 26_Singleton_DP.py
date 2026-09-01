# class SingletonClass:
#     __instance = None
#     def __init__(self, name):
#         if self.__instance==None:
#             self.name = name
#             SingletonClass.__instance = self
#         else:
#             raise TypeError('This is a Singletonclass.')
            
#     def whoareyou(self):
#         print(self.name)
    
# obj1 = SingletonClass('sakeeb')
# obj2 = SingletonClass('rahul')
# obj3 = SingletonClass('shrikant')

# print(id(obj1), id(obj2), id(obj3))


# class SingletonClass:
#     __instance = None
#     def __new__(cls, name):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             cls.__instance.name = name
#         return cls.__instance

#     def whoareyou(self):
#         print(self.name)

#     @classmethod
#     def resign(cls):
#         cls.__instance = None
    
# obj1 = SingletonClass('sakeeb')
# obj2 = SingletonClass('rahul')
# obj3 = SingletonClass('shrikant')

# print(id(obj1), id(obj2), id(obj3))

# obj1.whoareyou()
# obj2.whoareyou()
# obj3.whoareyou()

# obj1.resign()
# obj2 = SingletonClass('rahul')
# obj2.whoareyou()
# obj3.whoareyou()


