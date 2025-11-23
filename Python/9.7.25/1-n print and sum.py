#WAP to print 1 to n term by using for loop and print sum
n=int(input("Enter the Range = "))
s=0
for i in range(1,n+1,1):
    print(i,end=' ')
    s=s+i
print(" = ",s)
 