n=int(input("Enter the no ="))
c=0
rem=0
p=0
x=n
s=0
while n>0:
    c=c+1
    n=n//10
n=x
while n>0:
    rem=n%10
    p=pow(rem,c)
    s=s+p
    n=n//10
if x==s:
    print(x,"Is Armstrong no")
else:
    print(x,"Is not Armstrong no")