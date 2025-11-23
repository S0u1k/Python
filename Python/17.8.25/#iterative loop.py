#iterative loop
import csv
# Filtering data from a CSV file
x=input("Enter the file Name = ")
with open(x, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    filtered_rows = [i for i in csv_reader if int(i[2]) >=50] 
print(filtered_rows)