import csv
# Reading a CSV file
#f = "E:/xiics1st2024-25/College 25-26/Python/17.8.25/"
x=input("Enter the File Name = ")
with open(x, mode='r') as file:
    a = csv.reader(file)
    header = next(a)  # Skip the header row
    print(header)
    for i in a:
        print(i)