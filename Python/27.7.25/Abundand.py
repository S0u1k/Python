n = int(input("Enter the number = "))
i = 1
s = 0
while i < n:
    if n % i == 0:
        s += i
    i += 1
if s > n:
    print(n, "is an abundant number")
else:
    print(n, "is not an abundant number")
