#Write a program to calculate the sum of series 1 + 1/2 + 1/3+……+ 1/n using for loop.
n = int(input("Enter the range = "))
s = 0
for i in range(1, n+1):
    s = s + 1/i
print("Sum =", s)
