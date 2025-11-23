import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 8, 7])
x = np.where(arr%2 == 0)
print(x)