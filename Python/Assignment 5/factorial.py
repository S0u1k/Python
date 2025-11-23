#Write a program to calculate the factorial of a number using for loop
n=int(input("Enter the No. = "))
f=1
if n>=0:
    for i in range(n,0,-1):
        f=f*i
        if i==1:
            print(i,end=' ')
        else:
            print(i,end='*')
    print("=",f)
else:
    print("-ve no. factorial can't be possible")