#WAP to implement index()
n=int(input("Enter the Range = "))
li=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
y=int(input("Enter the No.="))
print(li.index(y))