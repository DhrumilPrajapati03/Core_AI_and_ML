import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[2,2])
print(a[1][1])
print(a.shape)
print(a.ndim)

#   0 1 2
# [[1,2,3] #0
#  [4,5,6] #1
#  [7,8,9]]#2

# slicing
b = np.array(['a','b','c','d','e','f','g','h'])
print(b[2:5])
print(b[:5])
print(b[::-1])
print(b[2:6:2])

a = [i for i in range(1,26)]
print(a)
k = np.array(a)
print(k)
j = k.reshape(5,5)
print(j)
