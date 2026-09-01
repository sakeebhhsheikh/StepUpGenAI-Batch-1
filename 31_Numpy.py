import numpy as np

# ndarray
#- Homogeneous Data Structure
# li = [1,2,3,4,5,6,7]
# arr = np.array(li)
# print(li)
# print(arr)

#Datatype Precedence :=>   str->complex->float->int->bool

# li = [1,2,3,4,5,6,7, 'a']
# arr = np.array(li)
# print(arr)

# li = [1,2,3,4,5,6,7,0.1]
# arr = np.array(li)
# print(arr)

#Attrubutes of Ndarray
#- ndim
#- shape
#- size
#- dtype

# li = [1,2,3,4,5,6,7,0.1]
# arr = np.array(li)
# print(arr)

# arr2d = np.array([[1,2],[3,4]])
# print(arr2d)
# print(arr2d.ndim)

# company = [
#     [
#         [100, 'sakeeb', 10000],
#         [101, 'rahul', 20000],
#         [102, 'snehal', 30000]
#     ],
#     [
#         [103, 'Ramesh', 30000],
#         [104, 'Shrikant', 40000],
#         [105, 'Jackson', 45000]
#     ]
# ]

# arr3d = np.array(company)
# print(arr3d)
# print(arr3d.ndim)
# print(arr3d[1][1][1])

#==> shape

# li = [1,2,3,4,5,6,7,0.1]
# arr = np.array(li)
# print(arr)
# print(arr.shape)

# arr2d = np.array([[1,2],[3,4]])
# print(arr2d)
# print(arr2d.shape)


# company = [
#     [
#         [100, 'sakeeb', 10000],
#         [101, 'rahul', 20000],
#         [102, 'snehal', 30000]
#     ],
#     [
#         [103, 'Ramesh', 30000],
#         [104, 'Shrikant', 40000],
#         [105, 'Jackson', 45000]
#     ]
# ]

# arr3d = np.array(company)
# print(arr3d)
# print(arr3d.shape)

#--> size ==> 

# company = [
#     [
#         [100, 'sakeeb', 10000],
#         [101, 'rahul', 20000],
#         [102, 'snehal', 30000]
#     ],
#     [
#         [103, 'Ramesh', 30000],
#         [104, 'Shrikant', 40000],
#         [105, 'Jackson', 45000]
#     ]
# ]

# arr3d = np.array(company)
# print(arr3d)
# print(arr3d.size)

#==> dtype

# li = [1,2,3,4,5,6,7]
# li = [1,2,3,4,5,6,7,0.1]
# li = [1,2,3,4,5,6,7,True]
# li = [1,2,3,4,5,6,7,'a']
# li = ['a','bb','c','dacv']
# arr = np.array(li)
# print(arr)
# print(arr.dtype)

#==> itemsize
# li = [1,2,3,4,5,6,7]
# arr = np.array(li)
# print(arr)
# print(arr.itemsize)

#-------------------------------------------
#--> Slicing : Index based slicing 

# arr[ position ]
# arr[ start : end+1 ]
# arr[ rowstart:rowend+1, colstart:colend+1]
# arr[ [row1, row2,...], colstart:colend+1]
# arr[ rowstart:rowend+1, [col1, col2, ...]]

# arr = np.array([[1,2,3,5],[4,5,6,7],[7,8,9,3],[4,2,6,7]])
# print(arr)
# print(arr[1])
# print(arr[1:3])
# print(arr[1:3])

# print(arr[:, 0])
# print(arr[:, 1:3])
# print(arr[1:3, 1:3])

# print(arr[[0,-1], 1:3])
# print(arr[[0,-1], [0,-1]])

#--------------------------------------
#==> Special function
#==> Conditional Slicing
#==> Element-wise operation
#==> Mathematical and statistical operation
#==> array generation
#==> array reshaping

#--------------------------------------
import timeit
import numpy as np
# li = [val**2 for val in range(1,10)]
# print(li)

# arr = np.array([val for val in range(1,10)])
# print(arr**2)

# np.arange(1,1000)**2
# arr =  np.arange(1,10000)
# print(arr)


# execution_time = timeit.timeit('[val**2 for val in range(1,10000)]', number=1000)
# print('list =' ,execution_time)
# execution_time = timeit.timeit(lambda:arr**2, number=1000)
# print('array =' ,execution_time)

#------------------------------------------
#->  arange
#->  zeros, zeros_like
#->  ones, ones_like
#->  full
#->  reshape
#->  revel
#->  linspace
#-> 

# arr = np.arange(1.5,10.5, 0.5)
# print(arr)

# arrz = np.zeros((3,4), dtype=int)
# print(arrz)

# arr = np.array([[1,2,3],[5,4,3.0]])
# arrz = np.zeros_like(arr)
# print(arrz)


# arrz = np.ones((3,4), dtype=int)
# print(arrz)

# arr = np.array([[1,2,3],[5,4,3.0]])
# arrz = np.ones_like(arr)
# print(arrz)


# arrz = np.full((3,4), 5)
# print(arrz)

# arr = np.array([[1,2,3],[5,4,3.0]])
# arrz = np.full_like(arr, 6)
# print(arrz)


#-------------------------------------

# arr = np.arange(1,13)
# print(arr)
# print(arr.shape)

# arr1 = arr.reshape((3,4), order='C')
# print(arr1)

# arr1 = arr.reshape((3,4), order='F')
# print(arr1)

# (2,2,3)

# arr1 = arr.reshape((2,2,3), order='C')
# print(arr1)

#--> ravel

# arr1 = np.arange(1,13).reshape((2,2,3), order='C')
# print(arr1)
# print(arr1.ravel(order='C'))
# print(arr1.ravel(order='F'))

#--> linspace

# arr = np.linspace(1, 10, 10)
# print(arr)
# arr = np.linspace(1, 10, 20)
# print(arr)
# arr = np.linspace(1, 10, 50)
# print(arr)
#-----------------------------------------------
#==> Mathematical Operation / Element-wise operation

# arr = np.arange(1, 11)
# arr1 = arr * 2
# print(arr1)

# arr = np.arange(1,10).reshape((3,3))
# print(arr)
# print(arr**2)

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[3,4],[1,2]])

# print(arr1 + arr2)
# print(arr1 / arr2)

# arr = np.array([1,2,3,5,0,6,4,3,1,0,4,5,6,8,2,5,8,9,0])
# print(arr)
# print(arr==True)

# arr = np.array([1,2,3,5,0,6,4,3,1,0,4,5,6,8,2,5,8,9,0])
# print(arr!=0)

#==> Slicing using Boolean Array
# arr = np.array([1,5,2,8,4,7,1,4,6,8,10,3])
# bool_li = [False,False,True,True,True,False,False,True,True,True,True,False]

# resarr = arr[[2,3,4,7,8,9,10]]
# print(resarr)

# resarr = arr[bool_li]
# print(resarr)

# print(arr%2==0)

#==> Conditional Slicing
# arr = np.array([1,5,2,8,4,7,1,4,6,8,10,3])
# resarr = arr[arr%2==0]
# print(resarr)

#----------------------------------------------
#-> all()
#-> any()
#-> min()
#-> max()
#-> matrix multiplication

#--> all()

# arr = np.array([1,2,3,5,0,6,4,3,1,0,4,5,6,8,2,5,8,9,0])
# arr = np.array([1,2,3,5,6,4,3,1,4,5,6,8,2,5,8,9])
# print(arr.all())


#--> any()
# arr = np.array([1,2,3,5,0,6,4,3,1,0,4,5,6,8,2,5,8,9,0])
# arr = np.zeros((10,), dtype=int)
# print(arr.any())

#--> Stistical Operation : 
# min, max, sum, mean, median, var, std, count, quantile, mode
# arr = np.arange(1,10).reshape((3,3))
# print(arr)

# print(arr.min())
# print(arr.max())
# print(arr.sum())
# print(arr.mean())
# print(np.median(arr))
# print(arr.var())
# print(arr.std())


# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
#===================================================================

# li = [2,3,4,6,1,8,7,5,2,4,6,2,3,4,5,2,3,4,2,3,3,3,2,2,5,5,7,7,4,4,3,3,2,2]
# print(sum(li)/len(li))
# arr = np.array(li)
# print(arr.mean())


# li = [2,1,3,4,5,2,2,2,3,2,3,4,500,1,2,2,3,4,2,1,2,3,1]
# li.sort()
# print(li)

# print(sum(li)/len(li))

#li = [60,60,60,60,60,60,60,60]
# li = [80,75,60,65,50,60,75,80]
# arr = np.array(li)

# var = ((arr - arr.mean())**2).sum() / arr.size
# print(var)

# print(arr.var())

# std = np.sqrt(var)
# print(std)

# print(arr.std())

#------------------------------------
# li = [2,1,3,4,5,2,2,2,3,2,3,4,500,1,2,2,3,4,2,1,2,3,1]
# arr = np.array(li)
# print('25% :', np.quantile(arr, 0.25))
# print('50% :', np.quantile(arr, 0.50))
# print('75% :', np.quantile(arr, 0.75))
# print('90% :', np.quantile(arr, 0.90))

# print(arr[arr>4].sum())
# print(arr[arr>4])

# index_pos = np.where(arr>4)
# print(index_pos)
# boolarray = np.where(arr>4, True, False)
# print(boolarray)
#------------------------------------
#Corelation : -1 -- 0 -- 1

# x = np.array([1,2,3,4,5])
# y = np.array([6,5,8,2,4])

# corr = np.corrcoef(x,y)
# print(corr)

#------------------------------------
#--> Co-variance : 
# x = np.array([1,2,3,4,5])
# y = np.array([2,4,6,8,10])

# covar = np.cov(x,y)
# print(covar)
#-------------------------------------
#=====================================
#==> Matrix Multiplication : 

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[2,3],[4,2]])

# print(arr1 * arr2)
# print(arr1 @ arr2)

#-----------------------------------

#==> Transpose

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)

# for i in range(3):
#     for j in range(3):
#         print(arr[j][i], end=' ')
    
# print(arr.T)

#-----------------------------------
# Frequency Distribution

import numpy as np

arr = np.loadtxt('mtcars.csv', delimiter=',', skiprows=1, usecols=range(1,12))
# print(arr.T)

# mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear,carb = arr.T
# print(mpg)

quantities = arr[:, [0,2,3,4,5,6]]
categories = arr[:, [1,7,8,9,10]]

# print(quantities.mean(axis=0))
# print(np.median(quantities, axis=0))

# print(categories.dtype)

categories = categories.astype(int)
# print(categories.dtype)

#Frequency Distribution in Numpy array :
#

import matplotlib.pyplot as plt

# gear = categories[:, -2]
# print(gear)
# frequencies = np.unique(gear, return_counts=True)
# print(frequencies)
# plt.bar(frequencies[0], frequencies[1])
# plt.xticks([3,4,5])
# plt.xlabel('Gears')
# plt.ylabel('Freq')
# plt.show()


# mpg = quantities[:, 0]
# frequencies = np.unique(mpg, return_counts=True)
# print(frequencies)
# plt.bar(frequencies[0], frequencies[1])
# plt.xlabel('mpg')
# plt.ylabel('Freq')
# plt.show()


#==> Histogram - bins

# arr = np.array([1,2,2,3,3,3,4,4,5])
# hist, bins = np.histogram(arr, bins=5)
# print(hist)
# print(bins)
# plt.bar(bins[:-1], hist)
# plt.xlabel('mpg')
# plt.ylabel('Freq')  
# plt.show()

# mpg = quantities[:, 0]
# plt.hist(mpg)
# plt.show()