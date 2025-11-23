#WAP to take input within a list & reverse the list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))
print(li)
li.reverse()
print(li)