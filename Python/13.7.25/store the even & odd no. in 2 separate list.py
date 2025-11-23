#WAP to take input within a list & store the even & odd no. in 2 separate list
li=[]
lieven=[]
liodd=[]
lineu=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))
print(li) # [0,75,-93,46,74]
for i in li:
    if i==0:
        lineu.append(i)
    elif i%2==0:
        lieven.append(i)
    else:
        liodd.append(i)
print("Even List =",lieven)
print("ODD List =",liodd)
print("Neutral List =",lineu)