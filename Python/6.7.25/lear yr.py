#WAP to check whether a year is leap year or not
yr=int(input("Enter the Year = "))
if yr%400==0:
    print(yr,"is Leap Year")
elif yr%4==0 and yr%100!=0:
    print(yr,"is Leap Year")
else:
    print(yr,"is NOT Leap Year")