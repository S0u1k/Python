#WAP to count a specific no. how many times in a list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))   
print(li)
x=int(input("Enter the No. to be searched for = "))
print(x,"Found",li.count(x),"No. of Times")