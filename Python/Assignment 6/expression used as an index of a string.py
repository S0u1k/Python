#Write a python program to demonstrate an expression used as an index of a string.
x=input("Enter the string = ")
for i in range(0,len(x),1):
    print("Character at index", i,"=", x[i],end=' ')
    print()