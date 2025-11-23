#WAP to store the even element from dictionary to list
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the Key = "))
    x[p]=int(input("Enter the No. = "))
print(x)
li=[]
for k,v in x.items():
    if v%2==0:
        li.append(v)
print(li)