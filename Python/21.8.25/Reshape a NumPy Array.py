### 4. Reshape a NumPy Array
import numpy as np
li=[]
n=int(input("Enter the range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
# Create a one-dimensional NumPy array
array = np.array(li)
print("Original Array:", array)

reshaped_array = array.reshape(2,3)
print("Reshaped Array:\n", reshaped_array)