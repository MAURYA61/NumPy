# Create Random values 

import numpy as np

#rand()

ran = np.random.rand(4)
print(ran)

#randn()

ran2 = np.random.randn(3)
ran3 = np.random.randn(3,5)
print(ran2)
print(ran3)


# ranf()

ran4 = np.random.ranf(4)
print(ran4)

# randint()
# randint(min,max,total_values)

ran5 = np.random.randint(0,30,4)
print(ran5)