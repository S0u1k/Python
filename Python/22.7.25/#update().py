#update()
x={'name':'Arisha','class':'B.Tech','sub':'python','marks':75}
x.update({'marks':85})
print(x)
x.update({'age':18})
print(x)
for k,v in x.items():
    print(k,":",v)