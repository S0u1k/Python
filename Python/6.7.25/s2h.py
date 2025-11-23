#WAP to convert second to hour
s=int(input("Enter the Second = "))
h=s//3600
s=s%3600
m=s//60
s=s%60
print("Hour = ",h,"Minute =",m,"Second =",s)