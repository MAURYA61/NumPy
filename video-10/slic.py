# slicing in 1-D array

import numpy as np 

var = np.array([1,2,3,4,5,6,7,8,9])

print(var)
print(var[1:])
print(var[:3])
print(var[1:6])
print(var[::2])
print(var[1:8:2])
print(var[1:8:3])


#Slicing in 2-D array
var1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(var1[0,3])
print(var1[0,:5])
print(var1[0,2:])
print(var1[1,3])
print(var1[1,:4])
print(var1[1,3:])
print(var1[2,4])
print(var1[2,:4])
print(var1[2,2:])