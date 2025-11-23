#Write a program to calculate the average of first n natural numbers using for loop
n=int(input("enter the range ="))
s=0
for i in range(1,n+1,1):
      print(i,end=' ')
      s=s+i
print("Sum =",s,"Average=",s/n)
