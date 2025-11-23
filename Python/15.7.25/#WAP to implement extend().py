#WAP to implement extend()
n=int(input("Enter the Range = "))
li=[]
li2=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. for the 1st List= ")))
print(li)
for i in range(0,n,1):
    li2.append(int(input("Enter the No. for the 2nd List= ")))
print(li2)
li2.extend(li)
print(li2)