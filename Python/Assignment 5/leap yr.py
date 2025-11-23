#Write a program to displays all leap year from 1900-2025 using for loop.
print("Leap years from 1900 to 2025 are:")
for yr in range(1900, 2025):
    if yr % 400 == 0:
        print(yr,'Is leap year')
    elif yr %4==0 and yr %100!=0:
        print(yr,"Is  lear year")