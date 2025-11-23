#WAP to copy duplicate element into another list
n=int(input("Enter the Range = "))
li=[]
li2 =[]
for i in range(0,n,1):
    li.append(input("Enter the Name = "))
print(li)  #['souvik','ankita','arisha','ankita','ayushi']
for i in li:
    if li.count(i) > 1 and i not in li2:
        li2.append(i)
print(li2)
print("Original list =",li)
print("Duplicate elements in another list =",li2)