n= int(input("Enter the no ="))
x=n
s=0
rem=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
    
print("Sum of digit of ",x,"is =",s)