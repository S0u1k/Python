#Write a python program to concatenate two strings sing + operator,append a string using += operator, repeat a string using * operator.# Program to demonstrate string operations

# Concatenate two strings using + operator
s1=input("Enter the 1st String =")
s2=input("Enter the 2nd String =")
result = s1 + " " + s2
print("Concatenation using + :", result)

# Append a string using += operator
s1 +=" "+ input("Enter the edited String =")
print("After appending using += :", s1)

# Repeat a string using * operator
repeat_str = input("Enter the  String =") * 3
print("Repetition using * :", repeat_str)
