# Copy  &  View

import numpy as np

# Copy
arr = np.array([1,2,3,4,5])
copy1 = arr.copy()

print("Original array : ",arr)
print("Copy array : ",copy1)


print()
# View

arr1 = np.array([1,2,3,4,5])
view1 = arr1.view()

print("Original : ",arr1)
print("View : ",view1)
print()

# Difference copy & view

# Chnages in copy

# chnages in original data copy data can not be change
arr2 = np.array([1,2,3,4,5])
co = arr2.copy()

arr2[1] = 10

print("Origonal : ",arr2)
print("Copy : ",co)
print()

# Changes in view

#Changes in original data copy data is also change

arr3 = np.array([1,2,3,4,5])
vi = arr3.view()

arr3[2] = 20

print("Original : ",arr3)
print("View : ",vi)