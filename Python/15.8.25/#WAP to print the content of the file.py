#WAP to print the content of the file 
x=input("Enter the File Name = ")
r=open("E:/xiics1st2024-25/College 25-26/Python/15.8.25/"+x,"r")
print(r.read())
r.close()