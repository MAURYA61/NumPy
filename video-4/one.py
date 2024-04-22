# Special type of array

import  numpy as np

# Zeros Element 

zero_arr = np.zeros(4)
print(zero_arr)

# Ones

one_arr = np.ones(4)
print(one_arr)

#Empty array 

em_arr = np.empty(4) # previous data are initilize automatically
print(em_arr)

# range 

rang_arr = np.arange(1,5)
range1 = np.arange(4)
print(rang_arr)
print(range1)


# Diagonal element

dia_arr = np.eye(3)
print(dia_arr)

dia2 = np.eye(3,4)
print(dia2)

# linspace

lin1 = np.linspace(1,20,num=5)
print(lin1)

lin2 = np.linspace(1,10,num=10)
print(lin2)

lin3 = np.linspace(2,20,num=10)
print(lin3)