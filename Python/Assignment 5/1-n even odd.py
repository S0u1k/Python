#Write a program to print all the numbers from m-n thereby classify them as even or odd using for loop.
n=int(input("enter the  1st range ="))
m=int(input("enter the 2nd range ="))
even_numbers = []
odd_numbers = []
print("Total number =")
for i in range(n,m+1,1):
    print(i,end=" ")
print()
for i in range(n,m+1,1):
     if i%2 == 0:
         even_numbers.append(i)
     else:
         odd_numbers.append(i)
print("\nEven Numbers =",even_numbers)
print("\nOdd Numbers =",odd_numbers)
