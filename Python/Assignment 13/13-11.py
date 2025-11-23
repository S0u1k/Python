#Assign. 13  -11
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    j=int(input("Enter the Key = "))
    x[j]=input("Enter the Name = ")
print("Dictionary =",x,sep='')
print(sorted(x))