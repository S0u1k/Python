#WAP to check whether a no is Pronic or not
n=int(input("Enter the No = "))
x=n
f=0
for i in range(1,n,1):
    if i*(i+1)==n:
        f=1
        break
if f==1:
    print(x,"is a Pronic No")
else:
    print(x,"is NOT a Pronic No")