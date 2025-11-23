#update using logic
x={1:5,2:10,4:15,5:20,6:25}
x[3]=17
print(x)
for i in sorted(x):
    print(i,":",x[i],end=" ")
print()
for k,v in x.items():
    p=v**2
    print(p,end=' ')