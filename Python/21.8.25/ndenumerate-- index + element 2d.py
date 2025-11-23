import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i, x in np.ndenumerate(arr):
  print("Index = ",i,"Value = ",x)