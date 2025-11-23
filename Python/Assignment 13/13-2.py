#Assign. 13  -2
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the Name = ")
print("Dictionary =",x,sep='')
for k,v in x.items():
    print(v)