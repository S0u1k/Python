#WAP to check whether a string is palindrome or not
x=input("Enter the String = ").upper()
print(x)
if x==x[::-1]:
    print("Palindrome String ")
else:
    print("NOT Palindrome String ")