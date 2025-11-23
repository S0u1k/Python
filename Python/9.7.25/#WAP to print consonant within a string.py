#WAP to print consonant within a string
x=input("Enter the String = ")
for i in x:
    if i not in 'AaEeIiOoUu':
        print(i,end=' ')