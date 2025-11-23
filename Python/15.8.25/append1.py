#(append)WAP to add/edit new content within the previously 
#created file or if the file is not created it will create a  new file
x=input("Enter the File Name = ")
r=open("E:/xiics1st2024-25/College 25-26/Python/15.8.25/"+x,"a")
a=input("Enter the Sentence = ")
r.write("\n")
r.write(a)
r.write("\n")
a=input("Enter the 2nd Sentence = ")
r.write(a)
r.close()
r=open("E:/xiics1st2024-25/College 25-26/Python/15.8.25/"+x,"r")
print(r.read())
r.close()