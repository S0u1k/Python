n=int(input("Enter the no ="))
x=n
s=0
c=0
rem=0
while n>0:
    rem=n%10
    c+=1
    n=n//10
n=x
while n>0:
    rem=n%10
    p=pow(rem,c)
    s=s+p
    c-=1
    n=n//10
if s==x:
    print(x,"Is disariyam no")
else:
    print(x,"Is not disariyam no")
    