n=int(input("enter the number ="))
f=0
for i in range(2,n,1):
    if n % i == 0:
        f = 1
        break
    
if(f==0 and n!=1):
 print(n,"Is prime number")
else:
   print(n,"Is not prime number")