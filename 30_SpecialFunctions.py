# eval
# zip
# enumerate
# map
# filter
# reduce

#--------------------------------------------

# a = eval('10')
# print(a, type(a))

# a = eval('10.5')
# print(a, type(a))

# name = 'sakeeb'
# res = eval('name')
# print(res)

#--------------------------------------------

# eno = [100,101,102,103, 104, 105]
# ename = ['Sakeeb','Shrikant','Snehal','Rahul','Max']

# Expected outcome : [(100, 'sakeeb'),(101, 'Shrikant'),(102, 'Snehal')]

# li = [(eno[i], ename[i])  for i in range(len(ename))]
# print(li)

# minlen = min([len(eno), len(ename)])
# li = [(eno[i], ename[i])  for i in range(minlen)]
# print(li)

# obj = zip(eno, ename)
# print(obj)

# li = list(zip(eno, ename))
# print(li)

# for t in zip(eno, ename):
#     print(t)


# eno = [100,101,102,103, 104, 105]
# ename = ['Sakeeb','Shrikant','Snehal','Rahul','Max']
# esal = [10000,200000,300000,400000,500000,60000]
# for t in zip(eno, ename, esal):
#     print(t)


# eno = [100,101,102,103, 104, 105]
# ename = ['Sakeeb','Shrikant','Snehal','Rahul','Max']
# dic = dict(zip(eno, ename))
# print(dic)

# dic = {100: 'Sakeeb', 101: 'Shrikant', 102: 'Snehal', 103: 'Rahul', 104: 'Max'}
# li = list(dic.items())
# print(li)

# eno, ename = zip((100, 'Sakeeb'), (101, 'Shrikant'), (102, 'Snehal'), (103, 'Rahul'), (104, 'Max'))
# print(eno, ename)

# li = [(100, 'Sakeeb'), (101, 'Shrikant'), (102, 'Snehal'), (103, 'Rahul'), (104, 'Max')]
# eno, ename = zip(*li)
# print(eno, ename)

#------------------------------------------------------------

# enumerate

# tup = ('Sakeeb', 'Shrikant', 'Snehal', 'Rahul', 'Max')
# for t in enumerate(tup, start=1000000):
#     print(t)

# for i, name in enumerate(tup):
#     print(i, name)

#------------------------------------------------------------
#==> lambda  ==>  Anonymous function

# def addme(a, b):
#     return a+b

# print(addme(10,20))


# def func(f):
#     a = eval(input('enter value:'))
#     b = eval(input('enter value:'))
#     res = f(a,b)
#     return res**2

# print(func(addme))

#----------------------------

# def func(f):
#     a = eval(input('enter value:'))
#     b = eval(input('enter value:'))
#     res = f(a,b)
#     return res**2

# # print(func(lambda x,y:x+y))

# addme = lambda x,y:x+y
# print(func(addme))

#----------------------------

# marks = [(100, 'sakeeb', 75),(101, 'Rahul', 44),(102, 'Sneha', 33),(103, 'Nitin', 88)]
# #Expected outcome : [(100, 'Pass'), (), (101, 'Pass'), (102, 'Fail'), (103, 'Pass')]

# def check_status(t):
#     if t[2]>=40:
#         res = 'Pass'
#     else:
#         res = 'Fail'
#     return (t[0], res)



# for res in map(check_status, marks):
#     print(res)

# print(map(check_status, marks))
# print(list(map(check_status, marks)))

# lambda t: 'Pass' if t[2]>=40 else 'Fail'
#==> Using Lambda
# print(list(map(lambda t: (t[0],'Pass') if t[2]>=40 else (t[0],'Fail'), marks)))

#Example  :
# def addme(a, b):
#     return a+b

# l1 = [10,20,30,40,50,60,70,80]
# l2 = [11,22,33,44,55,66,77,88,99]

#Expected Outcome = [21, 42, 63, 84, 105, 126, 147, 168]

# li = []
# for i in range(len(l1)):
#     li.append(addme(l1[i]+l2[i]))
# print(li)

#==> Using Lambda
# res = list(map(lambda a,b:a+b, l1, l2))
# print(res)

#-----------------------------------------------------------
#Map --> 
#Syntax : 
# map(function_obj, iterableobj-1, iterableobj-2, ......)

#-----------------------------------------------------------
#filter
# filter(functioobj, iterableobj)

#Example-1 :

# li = [1,2,3,4,5,6,7,8,9,10]
# res = filter(lambda x:True if(x%2==0) else False, li)
# print(li)
# print(list(res))

# Example-2 : 

# li = [1, 2, 0, 3, 4, 5, 0, '',6,7,'', 8, 9,10, None]
# res = filter(lambda x:True if x else False, li)
# print(li)
# print(list(res))

# li = [1, 2, 0, 3, 4, 5, 0, '',6,7,'', 8, 9,10, None]
# res = filter(None, li)
# print(li)
# print(list(res))

#----------------------------------------------------------------
# from functools import reduce

# li = [22,5,3,4,7,8,11,88,1,2,3,4,5,6,7,2,4,7,9,1,2,4,5,7,8,9,10]

# def addme(a,b):
#     return a+b

# val = reduce(addme, li)
# print(val)

# largest = reduce(lambda x, y:x if x>y else y, li)
# print(largest)
#----------------------------------------------------------------
# from itertools import accumulate, chain, cycle, permutations, product

# li = [3,4,6,1,2,7,9,2,5]
# res = accumulate(li)
# print(list(res))

# l1 = [1,2,3,4,5,6]
# l2 = [33,44,55,66,77,88]
# li = [[1,2,3,4,5,6], [33,44,55,66,77,88]]
# for val in chain(*li):
#     print(val)

# print(list(chain(*li)))

# import time
# l1 = [1,2,3,4,5,6]
# while True:
#     for val in l1:
#         print(val)
#         time.sleep(0.5)

# import time
# l1 = [1,2,3,4,5,6]
# for val in cycle(l1):
#     print(val)
#     time.sleep(0.5)

# s = 'ABCD'
# for val in product(s, repeat=2):
#     print(val)


# s = 'ABCD'
# for val in permutations(s, 2):
#     print(val)
