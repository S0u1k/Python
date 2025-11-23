#all func. in string
x="this is stRing prograMMing"
print(x.title())
print(x.capitalize())
x="rupa"
print(x.isalpha())
x="420"
print(x.isdigit())
x="rupa420"
print(x.isalnum())
x=" rupanjan dutta "
print(x.strip())
print(x.lstrip())
print(x.rstrip())
x="RUPANJAN"
print(x.islower())
print(x.isupper())
x="RupanJaN"
print(x.isupper())
print(x.upper())
print(x.lower())
print(x.index('n'))
#print(x.index('c'))
print(x.find('n'))
print(x.find('c'))
a="susmita pathak tui practice kor programming !!!! susmita valo achis"
b='susmita'
print(a.count(b))
x="     "
print(x.isspace())
x="souvik saha"
print(x.startswith('s'))
print(x.endswith('i'))
x="rupanjan dutta"
y=slice(2)
print(x[y])
y=slice(2,7)
print(x[y])
y=slice(2,len(x),2)
print(x[y])
x="arisha"
for i in x:
    print(ord(i),end=' ')