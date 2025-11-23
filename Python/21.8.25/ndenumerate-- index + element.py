import numpy as np
arr = np.array([10, 20, 30])
for i, x in np.ndenumerate(arr):
  print(i, x)