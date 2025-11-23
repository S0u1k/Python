# Circular Prime
n = int(input("Enter the No-"))
f = 0
a = n
c = 0
while True:
    c = 0
    print(a)
    for i in range(1, a + 1, 1):
        if a % i == 0:
            c += 1
    if c != 2:
        f = 1
        break
    else:
        S = str(a)
        P = S[1:] + S[0]
        a = int(P)
        if a != n:
            continue
        else:
            break

if f == 1:
    print(n, "is not a circular prime")
else:
    print(n, "is a circular Prime")