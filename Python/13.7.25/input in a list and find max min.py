#WAP to take input within a list & findout max, min element
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))   
print(li)
print("Minimum Element = ",min(li))
print("Maximum Element = ",max(li))