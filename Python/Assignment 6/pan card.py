'''Write a python program that takes user name and PAN card number as input.Validate the 
information using isX() function and print the details'''
x=input("Enter your 1st Name = ")
z=input("Enter your 2nd Name = ")
a=x.isalpha()
b1=z.isalpha()
if a==True and b1==True:
    print("Please enter your PAN card number:")
    y=input("Enter your PAN card number = ")
    b=y.isalnum()
    if b==True and len(y)==10:
        p=y[:5]
        a1=p.isupper()
        q=y[5:9]
        a2=q.isnumeric()
        r=y[9]
        a3=r.isupper()
        if a1==True and a2==True and a3==True:
            print("Name:", x)
            print("PAN Card Number:", y)
        else:
            print("Invalid PAN Card Number")
    else:
        print("Invalid PAN Card Number")
else:
    print("Invalid Name")