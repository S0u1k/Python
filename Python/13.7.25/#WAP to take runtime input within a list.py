#WAP to take runtime input within a list & print the list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    x=int(input("Enter the No. ="))
    li.append(x)   # 10,30,20,50,40
print(li)
li.sort()
print(li)
for j in li:
    print(j,end=' ')