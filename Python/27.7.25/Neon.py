n=int(input("Enter the no ="))
rem=0
s=0
sq=n*n
while sq>0:
    rem=sq%10
    s=s+rem
    sq=sq//10
if s==n:
    print(n,"Is neon no")
else:
    print(n,"Is not neon no")