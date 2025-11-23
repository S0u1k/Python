x = int(input("Enter the 1st number - "))
y = int(input("Enter the 2nd number - "))
cx = 0
i=1
while i<x:
    if x % i == 0:
        cx += 1
cy = 0
i=1
while i < y:
    if y % i == 0:
        cy += 1
if cx == 2 and cy == 2 and abs(x - y) == 2:
    print("Both are Twin Prime numbers")
else:
    print("Both are NOT Twin Prime numbers")