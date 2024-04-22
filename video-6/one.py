# dataType in numpy 
import numpy as np

var = np.array([1,2,3,4,5])
print("Date Type : ",var.dtype)

var2 = np.array([1.0,2.2,4.2,5.2])
print("Data Type : ",var2.dtype)

var3 = np.array(["a","d","f","g"])
print("Data Type : ",var3.dtype)

var4 = np.array(["a","b","c","d",2,3,4,5])
print("Data Type : ",var4.dtype)

# DataType Conversion

x = np.array([1,2,3,4,5],dtype = np.int8)
print("Data Type",x.dtype)

x2 = np.array([1,2,3,4],dtype = "f")
print("Data type : ",x2.dtype)


x3 = np.array([1,2,3,4],dtype = "S")
print("Data type : ",x3.dtype)


x4 = np.array([1,2,3,4,5])

new = np.float32(x4)

print("Data Type : ",x4.dtype)
print("Data Type : ",new.dtype)
print(x4)
print(new)



x5 = np.array([1,2,3,4,5])

new1 = np.float32(x5)

new_one = np.int_(new)

print("Data Type : ",x5.dtype)
print("Data Type : ",new1.dtype)
print("Data Type : ",new_one.dtype)
print(x4)
print(new1)
print(new_one)


x6 = np.array([1,2,3,4,5])

new2 = x6.astype(float)

print("Data Type : ",x6.dtype)
print("Data Type : ",new2.dtype)

print(x6)
print(new2)