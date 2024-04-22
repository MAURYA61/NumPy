# Search , Sort , Search Sort , Filter

''' Search  Array  '''

import numpy as np

var = np.array([1,2,3,4,5,6,7,8])
#               0,1,2,3,4,5,6,7
# print(var)

# x = np.where(var == 5)
x = np.where(var % 2 == 0)
# print(x)


''' Sort Array  '''

var1 = np.array([7,5,6,4,8,1,9,3,2])
# print("Original Array : ",var1)

so = np.sort(var1)
# print("Sorted Array : ",so)


''' Search sort  '''
# search and sort array is give us index where we insert the given value

var2 = np.array([1,2,3,4,6,7,8])
# print("Original Array : ",var2)

# sear = np.searchsorted(var2,5)
# sear = np.searchsorted(var2,[1,2,3])
sear = np.searchsorted(var2,[1,2,3],side = "left") # [0,1,2]
sear = np.searchsorted(var2,[1,2,3],side = "right")  #[1,2,3]
# print("Search and sort : ",sear)


''' Filter array '''

var = np.array(['a','s','d','f'])
f = [True,False,True,False]
# print(var)
new = var[f]
# print(new)
# print(type(new))

arr = np.array([41,42,43,44])
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)