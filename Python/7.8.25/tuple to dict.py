#convert tuple to dict.
t1=(10,20,30,40,50,60)
d1={}
d1=dict(zip(t1[::2], t1[1::2]))
print(d1)