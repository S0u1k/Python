# WAP to implement ZIP

n = int(input("Enter the 1st list Range = "))
x = []
for i in range(0, n):
    x.append(input("Enter the string = "))

m = int(input("Enter the 2nd list Range = "))
y = []
for i in range(0, m):
    y.append(input("Enter the string = "))

Z = list(zip(x, y))
print(Z)