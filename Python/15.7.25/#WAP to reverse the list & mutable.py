#WAP to reverse the list & mutable 
n=int(input("Enter the Range = "))
li=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
#y=input("Enter the String = ")
li[2]=input("Enter the String = ")
print(li)
print(li[::-1])