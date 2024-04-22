# Arithmetic operation

import numpy as np

# Arthmetic Operation on 1-D array

var = np.array([4,4,4,4,4])

a = var + 3
b = var - 3
c = var / 2
d = var % 2
e = var * 2
f = var ** 2

print("Sum : ",a)
print("Sub : ",b)
print("Div : ",c)
print("Mod : ",d)
print("Multi : ",e)
print("Power : ",f)

# using function

x = np.array([2,2,2,2])
y = np.array([2,2,2,2])

print("Sum : ",np.add(x,y))
print("subtract : ",np.subtract(x,y))
print("multiply : ",np.multiply(x,y))
print("divide : ",np.divide(x,y))
print("mod : ",np.mod(x,y))
print("power : ",np.power(x,y))


print("reciprocal : ",np.reciprocal(var))
print("reciprocal : ",np.reciprocal(x))