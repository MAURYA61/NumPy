import numpy as np

var = np.array([1,2,3])
print(var.shape)
print(var)

var1 = np.array([[1],[2],[3]])
print(var1)
print(var1.shape)


var2 = np.array([[1],[2]])
print(var2.shape)

var3 = np.array([[1,2,3],[1,2,3]])
print(var3.shape)

print(var2+var3)