n=int(input("Enter the no="))
x=n
c=0
p=0
s=0
while n>0:
    c+=1
    n=n//10
sq=x*x
p=pow(10,c)
a=sq%p
b=sq//p
if (a+b) == x:
    print(x,"Is kaprekar no")
else:
    print(x,"Is not kaprekar no")
    