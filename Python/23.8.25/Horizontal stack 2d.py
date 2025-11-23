import numpy as np
arr1 = np.array([[1, 2, 3],[2,3,4]])
arr2 = np.array([[4, 5, 6],[5,6,7]])
arr = np.hstack((arr1, arr2))
print(arr)

'''👉 So the rule:

For 2D and higher → hstack = concatenate(..., axis=1)

For 1D → hstack = concatenate(..., axis=0)'''