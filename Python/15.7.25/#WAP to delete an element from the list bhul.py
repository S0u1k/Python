#WAP to delete an element from the list
n=int(input("Enter the Range = "))
li=[]
j=0
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
x=int(input("Enter the No. to be deleted = "))
for i in range(0,n,1):
    if li[i]==x:
        j=1
        break
if j==1:
    del(li[i])
    print(li)
else:
    print("Not Found")