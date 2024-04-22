# Shape and Reshap

import numpy as np
# Shape

x = np.array([[1,2,3,4],[5,6,7,8]])

print(x)
print(x.shape)
print(x.ndim)


y = np.array([1,2,3,4],ndmin = 5)
print(y)
print(y.shape)
print(y.ndim)


# reshape

print("RESHAPE")
a = np.array([1,2,3,4,5,6])
print(a)
print(a.shape)
print(a.ndim)

b = a.reshape(3,2)
print(b)
print(b.shape)
print(b.ndim)


x1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x1)
print(x1.ndim)

x2  = x1.reshape(2,3,2)
print(x2)
print(x2.ndim)

one = x2.reshape(-1)
print(one)
print(one.ndim)