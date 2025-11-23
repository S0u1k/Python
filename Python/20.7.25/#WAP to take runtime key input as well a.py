#WAP to take runtime key input as well as value input
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the Key = "))
    x[p]=input("Enter the Name = ")
print(x)
for k,v in x.items():
    print(k,"=",v)