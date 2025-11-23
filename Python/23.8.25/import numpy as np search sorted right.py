import numpy as np
arr = np.array([6, 9, 8, 7])
x = np.searchsorted(arr, 7, side='right')
print(x)