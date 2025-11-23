import numpy as np
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. for 1st List = ")))
    li2.append(int(input("Enter the No. for 2nd List = ")))
print("List 1 = ",li)
print("List 2 = ",li2)
arr = np.array(li)
arr1=np.array(li2)
x = np.lcm(arr,arr1)
y = np.gcd(arr,arr1)
print("LCM = ",x)
print("GCD = ",y)