#Split function 

import numpy as np

var = np.array([1,2,3,4,5,6])
new = np.array_split(var,3)
# print(new)
# print(new[0])


var1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
new1 = np.array_split(var1,4)
# print(new1)
# print(new1[0])

# arr1 = np.array_split(var1,3,axis=1)
arr1 = np.array_split(var1,3,axis=0)
print(arr1)