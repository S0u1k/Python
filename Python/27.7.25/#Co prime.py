#Co prime
x=int(input("Enter the 1st no ="))
y=int(input("Enter the 2nd no ="))
i=1
gcd=0
while i<=x and i<=y:
    if x%i==0 and y%i==0:
        gcd=i
    i+=1
if gcd == 1:
    print("Co  prime")
else:
    print("Is not co prime")