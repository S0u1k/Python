x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the Name = ")
print(x)
for c in x:
    if c>1:
        print("one key present")
        break