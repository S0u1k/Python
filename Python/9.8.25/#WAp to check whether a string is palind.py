#WAp to check whether a string is palindrome or not
x=input("Enter the Name = ")
#print(x.upper())
#print(x[::-1].upper())
if x.upper()==x[::-1].upper():
    print("Palindrome String")
else:
    print("NOT Palindrome String")