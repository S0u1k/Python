import numpy as np
arr = np.array([9, 7, 8,10, 2,3])
x = np.searchsorted(np.sort(arr), 7)    #2,3,7,8,9,10
print(x)