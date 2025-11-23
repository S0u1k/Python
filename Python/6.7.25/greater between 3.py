a=int(input("enter the number ="))
b=int(input("enter the number ="))
c=int(input("enter the number ="))
if a>b and a>c:
     print("1st number is greatest")
elif b>c and b>a:
     print("2nd number is greatest")
elif a==b and a==c:
     print("All are equal")
else:
     print("3rd number is greatest")