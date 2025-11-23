#WAP to delete the element keywise
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the Key = "))
    x[p]=input("Enter the Name = ")
print(x)
f=0
a=int(input("Enter the Key u wan't to delete = "))
for k,v in x.items():
    if k==a:
        f=1
        break
if f==1:
    del(x[k])
    print(x)
else:
    print("Element Not Found")