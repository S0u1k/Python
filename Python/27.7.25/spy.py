n=int(input("Enter the no="))
x=n
s=0
f=1
while n>0:
    rem=n%10
    s=s+rem
    f=f*rem
    n=n//10
if s==f:
    print(x,"Is Spy no")
else:
    print(x,"Is not Spy no")