n=int(input("Enter the no ="))
s=0
x=n
rem=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
if x%s==0:
    print(x,"Harshad no")
else:
    print(x,"is not Harshad no")