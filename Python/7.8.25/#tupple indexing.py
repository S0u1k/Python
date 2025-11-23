#tupple indexing
t1=(0,1,2,3,4,5,6,7,8,9,'d','e','e','p','t','u','i','m','a','r','k','h','a','b','i','d','e','e','p')
for i in range(0,len(t1),1):
    if t1[i]=='d':
        print(t1[i],"present at ",i,"index & position = ",i+1)
print("d present at ",t1.index('d'))
print("d present at ",t1.index('d',12))
print("d present at ",t1.index('d',12,26))