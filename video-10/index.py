import numpy as np

var = np.array([9,8,7,6])
#               0,1,2,3,4
#               -4-3,-2,-1

# print(var[1])
# print(var[0])
# print(var[-1])
# print(var[-3])


var1 = np.array([[3,4,5,4],[9,8,7,6]])
# print(var1.ndim)
# print(var1)
# print(var1[0,1])
# print(var1[1,0])


var2 = np.array([[[1,2],[6,7]]])
print(var2.ndim)
print(var2)
print(var2[0,1,1])