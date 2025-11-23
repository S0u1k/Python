#WAP to delete an element from the list
n=int(input("Enter the Range = "))
li=[]
j=0
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
x=int(input("Enter the No. to be deleted = "))
for i in li:
    if i==x:
        j=j+1
        li.remove(i)
if j>=1:
    print(li)
    print("deleted",x,",",j,"Times")
else:
    print("Not Found")