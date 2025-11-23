n=int(input("Enter the no ="))
s=s1=0
x=n
while n>0:
    rem=n%10
    s=s+rem
    n=n//10

while s>0:
    rem=s%10
    s1=s1+rem
    s=s//10

if s1==1:
    print(x,"Is magic no")
else:
    print(x,"Is not magic no")