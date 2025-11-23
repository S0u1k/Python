x = int(input("Enter the 1st number - "))
y = int(input("Enter the 2nd number - "))

# Count factors of x
cx = 0
i = 1
while i < x:
    if x % i == 0:
        cx += 1
    i += 1

# Count factors of y
cy = 0
i = 1
while i < y:
    if y % i == 0:
        cy += 1
    i += 1

# Check twin primes
if cx == 1 and cy == 1 and abs(x - y) == 2:
    print("Both are Twin Prime numbers")
else:
    print("Both are NOT Twin Prime numbers")
