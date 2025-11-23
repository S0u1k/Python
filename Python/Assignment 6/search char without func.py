'''Write a python program hat finds whether a given character 
is present in a string or not.In case it is present it prints 
the index at which it is present. Do not use built in function to search the key.'''

s = input("Enter a string: ").upper()
ch = input("Enter a character to search: ").upper()

f=0  

for i in range(len(s)):
    if s[i] == ch:
        print(" Character", ch, "found at index", i)
        f=1
        break  

if f==0:
    print(" Character", ch, "not found in the string.")
