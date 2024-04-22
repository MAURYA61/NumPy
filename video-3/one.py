# Array creation in numpy

import numpy as np

# x = [1,2,3,4]

# y = np.array(x)
# print(y)
# print(type(y))



l = []

# for i in range(1,5):
    # num = int(input("Enter number : "))
    # l.append(num)

# arr = np.array(l)
# print(arr)
# print(type(arr))


# Dimension in ndArray

# 1-D
x = np.array([1,2,3,4])
print(x)
print(x.ndim)

# 2 -D
a = np.array([[1,2,3,4]])
print(a)
print(a.ndim)

b = np.array([[1,2,3,4],[1,2,3,4]])
print(b)
print(b.ndim)

# 3 - D
c = np.array([[[1,2,3,4]]])
print(c)
print(c.ndim)

d = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(d)
print(d.ndim)

# Multi - D
e = np.array([1,2,3,4] , ndmin = 10)
print(e)
print(e.ndim)