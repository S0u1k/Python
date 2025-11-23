x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the key = "))
    x[p]=input("Enter the Name = ")
print(x)
y=int(input("Enter the key = "))
if y in x:
    print(y,"Is in dictionary")
else:
    print(y,"Is not  in dictionary")