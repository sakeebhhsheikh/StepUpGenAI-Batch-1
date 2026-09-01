from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def update(self, msg) : pass

class ObserverDP(Interface):
    __registered_user = []
    # def __init__(self, userobj):
    #     self.__registered_user.append(userobj)

    def register(self, userobj):
        self.__registered_user.append(userobj)
    
    def unregister(self, userobj):
        for i in range(len(self.__registered_user)):
            if userobj is self.__registered_user[i]:
                removed_user = self.__registered_user.pop(i)
                print(f'Hello you have been removed')
    
    def update(self, msg):
        for userobj in self.__registered_user:
            userobj.update(msg)

class NSE(Interface):
    def update(self, msg):
        print(f'Hello, NSE we have an update : {msg}')

class BSE(Interface):
    def update(self, msg):
        print(f'Hello, BSE we have an update : {msg}')

obj = ObserverDP()
nse = NSE()
bse = BSE()

obj.register(nse)
obj.register(bse)

obj.update('CEO of XYZ company has resigned.')