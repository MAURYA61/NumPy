import numpy as np

# %timeit np.arange(1,9)**4

# 3.08 µs ± 1.27 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each)


# %timeit [j**4 for j in range(1,9)]

# 4.13 µs ± 553 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)