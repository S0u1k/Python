n = int(input("Enter the number = "))
x = n
i = 1
print("Factors of", n, "are =")
while i < n:
    if n%i ==0:
        print(i,end=" ")
    i+=1