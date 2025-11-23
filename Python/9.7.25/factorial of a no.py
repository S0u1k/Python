'''
   WAP to calculate factorial of a no.
      5--->5*4*3*2*1  =120
'''
n=int(input("Enter the No. = "))
f=1
if n>=0:
    for i in range(n,0,-1):
        f=f*i
        if i==1:
            print(i)
        else:
            print(i,end='*')
    print("Factorial is =",f)
else:
    print("-ve no. factorial can't be possible")