#Iterating NumPy Array 

import numpy as np


# 1-D array
x = np.array([9,8,7,6,5,4,3,2])

for item in x:
    print(item)

for idx,i in np.ndenumerate(x):
    print(idx,i)

print()

# 2-D array

var = np.array([[9,7,6,4],[7,5,3,7]])
print(var)

for i in var:
    print(i)

print()

for i in np.nditer(var):
    print(i)

print()

for idx,i in np.ndenumerate(var):
    print(idx,i)

print("Change The dataType : ")

for i in np.nditer(var , flags = ["buffered"],op_dtypes = ['S']):
    print(i)

print()
# 3-D array

var1 = np.array([[[1,2,3],[1,2,3]]])
print(var1)

for i in var1:
    print(i)


for  i in np.nditer(var1):
    print(i)

print()

for idx,i in np.ndenumerate(var1):
    print(idx,i)


print()

arr = np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(arr)

for idx,i in np.ndenumerate(arr):
    print(idx,i)