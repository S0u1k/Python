n = int(input("Enter the number = "))
i = 1
while i * (i + 1) <n:
    i += 1
    print(i,end=" ")
print()
if i * (i + 1) == n:
    print(n, "is a pronic number")
else:
    print(n, "is not a pronic number")
