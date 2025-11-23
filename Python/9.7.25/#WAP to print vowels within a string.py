#WAP to print vowels within a string
x=input("Enter the String = ")
for i in x:
    if i in 'AaEeIiOoUu':
        print(i,end=' ')