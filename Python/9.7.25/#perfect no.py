# Perfect number
n = int(input("Enter the no = "))
s = 0
for i in range(1, n, 1):
    if n % i == 0:
        print(i, end=" ")
        s = s + i              
print()  
if s == n:
    print(n, "is Perfect no")
else:
    print(n, "is not Perfect no")
