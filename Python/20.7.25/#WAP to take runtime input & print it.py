#WAP to take runtime input & print it
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the Name = ")
print(x)
for k,v in x.items():
    print(k,"=",v)