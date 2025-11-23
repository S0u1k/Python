#WAP to print 1 to n term by using for loop
n=int(input("Enter the Range = "))
for i in range(n):
    print(i,end=' ')
print()
for i in range(1,n+1,1):
    print(i,end=' ')
print()
for i in range(1,n+1,2):
    print(i,end=' ')
print()
# n-1 print
for i in range(n,0,-1):
    print(i,end=' ')