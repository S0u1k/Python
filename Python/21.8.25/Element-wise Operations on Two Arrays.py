### 2. Element-wise Operations on Two Arrays
import numpy as np
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. for 1st List = ")))
    li2.append(int(input("Enter the No. for 2nd List = ")))
print("List 1 = ",li)
print("List 2 = ",li2)
# Create two NumPy arrays
array1 = np.array(li)
array2 = np.array(li2)

# Perform element-wise operations
sum_array = array1 + array2
difference_array = array1 - array2
product_array = array1 * array2
quotient_array = array1 / array2

print("Sum:", sum_array)
print("Difference:", difference_array)
print("Product:", product_array)
print("Quotient:", quotient_array)