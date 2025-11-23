#Write a python program to add a new item in the dictionary.
a=int(input("Enter the range of the Dictionary = "))
x={}
for i in range(1,a+1,1):
    b=int(input("Enter the No of the Key ="))
    x[b]=input("Enter the Value of the key = ")
print("The dictionary is ", x)
c=int(input("Enter the new Key="))
x[c]=input("Enter the Value of the key")
print("The New Dictionary will be ",x)