#WAP to print the multiplication table of a no.
n=int(input("Enter the No. = "))
print("------------------------------")
print("\tMultiplication Table")
print("------------------------------")
for i in range(1,11,1):
    m=n*i
    print("\t",n,"x",i,"=",m)