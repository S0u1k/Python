'''Write a python program that counts the occurrences of a character in a string. Do not use built in function'''

x= input("Enter a string: ").upper()
ch = input("Enter a character to count: ").upper()
c=0
for i in x:
    if i == ch:
        c+= 1
print("Character", ch, "occurs", c, "time(s) in the string.")
