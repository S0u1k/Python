#Write a program to print the multiplication table of n, where n is entered by the user using for loop.
n=int(input("Enter the No. = "))
print("------------------------------")
print("\tMultiplication Table")
print("------------------------------")
for i in range(1,11,1):
    m=n*i
    print("\t",n,"x",i,"=",m)