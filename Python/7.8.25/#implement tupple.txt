#implement tupple
t1=()
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    x=int(input("Enter the No. = "))
    t1=t1+(x,)
print(t1)