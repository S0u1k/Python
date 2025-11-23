#WAP to take input within a list & store the postive and negative no. in 2 separate list
li=[]
lipos=[]
lineg=[]
lineu=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. =")))
print(li)
for i in li:  # [15,-23,68,-75,45]
    if i>0:
        lipos.append(i)  #15,68,45
    elif i==0:
        lineu.append(i)
    else:
        lineg.append(i)  #-23,-75
print("Positive List =",lipos)
print("Negative List =",lineg)
print("Neutral List =",lineu)