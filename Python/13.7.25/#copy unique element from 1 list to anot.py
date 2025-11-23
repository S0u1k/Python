#copy unique element from 1 list to another list
# [10,20,30,10,20,50]
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))   
print(li)
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)