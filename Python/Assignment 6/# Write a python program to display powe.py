# Write a python program to display powers of a number without using formatting character.

num = int(input("Enter the number: "))
limit = int(input("Enter the power limit: "))

print("Powers of", num, "are:")

for i in range(1, limit + 1):
    print("Power", i, "=", num ** i)
