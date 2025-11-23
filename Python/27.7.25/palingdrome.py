n=int(input("Enter the no ="))
rev =0
x=n
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if x==rev:
    print(x,"Palingdrome no")
else:
    print(x," is not Palingdrome no")