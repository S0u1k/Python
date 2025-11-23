#WAP to check wheter a no is autopolymorphic or not
 #5-->5^2=25%10=5
  #6-->6^2=36%10=6 

x=int(input("Enter the number="))
if (x*x)%10 ==x or (x*x)%100 == x:
    print(x,"is autopolymorphic no")
else:
    print(x,"is not autopolymorphic no")