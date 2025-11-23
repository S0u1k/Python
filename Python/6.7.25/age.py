a = int(input("Enter the age = "))
if a > 0 and a < 6:
    print("Infant")
elif a > 6 and a <= 12:
    print("Child")
elif a > 12 and a <= 18:
    print("Teenager")
elif a > 18 and a <= 35:
    print("Young aged")
elif a > 35 and a <= 60:
    print("Middle aged")
elif a > 60 and a <= 100:
    print("Old aged")
elif a > 100:
    print("Not human")
else:
    print("N/A")
