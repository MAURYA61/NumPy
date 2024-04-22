#Transpose , Swapaxes , Inverse , power , Determinate

import numpy as np

'''Transpose'''
var = np.matrix([[1,2,3],[4,5,6]])
# print("Original Matrix ")
# print(var)
# print("After transpose ")
# print(np.transpose(var))
# print(var.T)

'''Swapaxes'''

# the swapaxes matrix is chnaged row into column and column into row 

var1 = np.matrix([[1,2],[3,4]])
# print("Original Matrix")
# print(var1)   
# print("After swapaxes")
# print(np.swapaxes(var1,0,1))
# print(np.swapaxes(var1,1,0))


'''Inverse'''

var2 = np.array([[2,3],[4,5]])
# print("Original matrix ")
# print(var2)
# print("After Inverse")
# print(np.linalg.inv(var2))


'''power''' # np.linalg.matrix_power(var,n) , n>0 , n<0 , n=0 

# n = 0 => I 
# n > 0 => power(multiply)
# n < 0 => inverse*power


var3 = np.matrix([[2,3],[4,5]])
# print("Original matrix")
# print(var3)
# print("Power matrix")
# print(np.linalg.matrix_power(var3,2))
# print(np.linalg.matrix_power(var3,0))
# print(np.linalg.matrix_power(var3,-2))


'''Determinante'''
# np.linalg.det(var)

var4 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("Original")
print(var4)
print("Determinate")
print(np.linalg.det(var4))