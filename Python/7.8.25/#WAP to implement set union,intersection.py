#WAP to implement set union,intersection , difference
st1=set()
st2=set()
st3=set()
n=int(input("Enter the range = "))
for i in range(0,n,1):
    st1.add(int(input("Enter the No. for 1st Set = ")))
for i in range(0,n,1):
    st2.add(int(input("Enter the No. for 2nd Set = ")))
print("Set 1 = ",st1)
print("Set 2 = ",st2)
st3=st1 | st2
print("Set 3 Union = ",st3)
st3=st1 & st2
print("Set 3 Intersection = ",st3)
st3=st1 - st2
print("Set 3 Difference(st1-st2) = ",st3)
st3=st2 - st1
print("Set 3 Difference(st2-st1) = ",st3)