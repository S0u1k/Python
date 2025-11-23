#twisted prime
n = int(input("Enter a number: "))
f = 0
i = 2
x=n
y=n
s=0

while i < n:
    if n % i == 0:
        f = 1
        break
    i += 1
n=x
while n > 0:
    rem=n%10
    s=s*10+rem
    n=n//10

i=2
k=0
n=s
while i < n:
    if n % i == 0:
        print(n)
        k = 1
        break
    i += 1
if f==0 and k==0 and y!=1:
    print("Twisted prime")
else:
    print("Not twisted prime no")    