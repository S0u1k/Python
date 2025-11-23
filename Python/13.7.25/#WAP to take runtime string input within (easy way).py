#WAP to take runtime string input within a list & print the list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter the String ="))   
print(li)
li.sort()
print(li)
for j in li:
    print(j,end=' ')