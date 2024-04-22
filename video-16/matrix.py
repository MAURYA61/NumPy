# Matrix in ndarray

import numpy as np

var = np.matrix([[1,2,3],[4,5,6]])
print(var)
print(type(var))


# array

var1 = np.array([[1,2,3],[4,5,6]])
print(var1)
print(type(var1))

# multiply in matrix

var2 = np.matrix([[1,2],[3,4]])
var3 = np.matrix([[5,6],[3,4]])
print(var2)
print(var3)
print(type(var1))
print(var2*var3)
print(var2.dot(var3))