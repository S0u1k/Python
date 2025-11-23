# 1. Create and Manipulate a NumPy Array
import numpy as np
# Create a NumPy array
li=[]
n=int(input("Enter the range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
array = np.array(li)
print("Original Array:", array)
add = array + 5
p = array * 2

print("Array after adding 5:", add)
print("Array after multiplying by 2:", p)