# WAP to print the concatenate version of the String
x=input("Enter the 1ST name of the User = ")
y=input("Enter the MIDDLE name of the User = ")
z=input("Enter the LAST name of the User = ")
fst=x[0].upper()+'.'
mid=y[0].upper()+'.'
last_lst=z[0].upper()
print("Concatenate of The String = ",fst+mid+last_lst,end="")
for i in range(1,len(z),1):
    print(z[i],end="")