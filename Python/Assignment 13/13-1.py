#Assign. 13  -1
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=i*2
print(x)
for k,v in x.items():
    print(k,":",v)