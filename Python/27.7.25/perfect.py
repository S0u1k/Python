n=int(input("enter the no ="))
i=1
s=0
while i<=n/2:
    if n%1==0:
        s=s+i
    i+=1
if s==n:
    print(n,"Is perfect no ")
else:
    print(n,"Is not perfect no ")