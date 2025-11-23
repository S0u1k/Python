'''
  WAP to print tribonacci series 
  1 1 1 3 5 9 17 31 57 --n

'''
n=int(input("Enter the range ="))
a=1;b=1;c=1
print(a,b,c,end=" ")
for i in range(1,n-2,1):
    s=a+b+c
    print(s,end=' ')
    a=b
    b=c
    c=s