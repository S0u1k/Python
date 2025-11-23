'''
   WAP to check whether  no. is buzz or not
   77,147,217,287,357,427,497,567,637,707
   %7==0    %10==7
   17,35,
'''
x=int(input("Enter the No. = "))
if x%7==0 and x%10==7:
    print(x,"is Buzz No.")
else:
    print(x,"is NOT Buzz No.")