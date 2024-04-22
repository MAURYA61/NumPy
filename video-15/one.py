# Insert and Delete Function

import numpy as np 

''' Insert '''
# 1 - D Array
var = np.array([1,2,4,6,7])
# print("Original Array : ",var)

# ins = np.insert(var,2,3)
# ins = np.insert(var,2,(3,40))
# ins = np.insert(var,(2,4),(3))
# ins = np.insert(var,(2,4),3.5)
# print("After Inserting : ",ins)


# 2 - D Array

var1 = np.array([[1,2,3],[4,5,6]])
print("Original Array ")
print(var1)

# ins1 = np.insert(var1,2,6,axis=1)
# ins1 = np.insert(var1,2,6,axis=0)
# ins1 = np.insert(var1,2,[22,23],axis=1)
ins1 = np.insert(var1,2,[22,23,24],axis=0)
print("After Inserting Value ")
print(ins1)


#we can also use append function for inserting a value in array

print("Append Function ")

var2 = np.array([1,2,3,4])
# print("Original Array ",var2)
# x = np.append(var2,7)
# x = np.append(var2,(7,5),axis=0)
# print("After appending : ",x)

var3 = np.array([[1,2,3],[4,5,6]])
print("Original Array : ")
print(var3)

x1 = np.append(var3,[[7],[8]],axis=1)
print("After appending : ")
print(x1)