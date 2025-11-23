#WAP to insert element in specific index
n=int(input("Enter the Range = "))
li=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
li.insert(2,int(input("Enter the No. = ")))
print(li)