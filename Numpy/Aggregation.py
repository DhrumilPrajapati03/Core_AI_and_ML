import numpy as np

# l = [1,2,3,4,5,6,-5,-9]
# a = np.array(l,ndmin=4)
# print(a)
# print(a.shape)
# print(a.ndim)
# minimum = a.min()
# print(minimum)

# argmini = a.argmin()
# print(argmini)

# maximum = a.max()
# print(maximum)

# argmaxi = a.argmax()
# print(argmaxi)

# add = a.sum()
# print(add)

# meann = a.mean()
# print(meann)

# s = a.std()
# print(s)

array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
add1 = array2d.sum(axis=0) #columns & axis=1 --> rows
print(array2d)
print(add1)