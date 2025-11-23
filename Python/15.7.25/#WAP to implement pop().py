#WAP to implement pop()
n=int(input("Enter the Range = "))
li=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
li.pop()
print(li)
li.pop(2)
print(li)