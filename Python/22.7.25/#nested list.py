#nested list
li=[]
li2=[]
n=int(input("Enter the range = "))
for i in range(0,n,1):
    li.append(input("Enter the Name for 1st List= "))

    li2.append(input("Enter the Name for 2nd List= "))
print("1st List = ",li)
print("2nd List = ",li2)
for i in li:
    for j in li2:
        print(i,j)