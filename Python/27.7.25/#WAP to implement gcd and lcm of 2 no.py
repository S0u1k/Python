#WAP to implement gcd and lcm of 2 no
a=int(input("Enter the 1st No = "))
b=int(input("Enter the 2nd No = "))
x,y=a,b
while b != 0:
        temp = b
        b = a % b
        a = temp
print(f"GCD is {a}")
lcm = (x*y) // a
print(f"LCM is {lcm}")