'''
   Acromatic String
   input --> arisha paul chowdhury
   output--> A.P.C.
'''
x=input("Enter the String = ").upper()
x=" "+x
print(x)
print(len(x))
for i in range(0,len(x),1):
    if x[i] ==' ':
        print(x[i+1],".",end='')