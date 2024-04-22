#NumPy Array function Join & Split

#Join function

import numpy as np

# 1-D array

var = np.array([1,2,3,4])
var1 = np.array([1,2,3,4])

new_array = np.concatenate((var,var1))
# print(new_array)

# 2-D array

var2 = np.array([[1,2],[1,2]])
var3 = np.array([[1,2],[1,2]])

new = np.concatenate((var2,var3))
# print(new)

 # inBuilt function 

#  h = horizontal
#  v = vertical

var4 = np.array([[[1,2],[3,4]]])
var5 = np.array([[[5,6],[7,8]]])

# new1 = np.stack((var4,var5),axis=1)
# new1 = np.stack((var4,var5),axis=0)
# new1 = np.hstack((var4,var5))
new1 = np.vstack((var4,var5))
print(new1)