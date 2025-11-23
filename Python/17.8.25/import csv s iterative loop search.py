import csv
# Filtering data from a CSV file
x=input("Enter the file Name = ")
y=input("Enter the Name you want to search = ")
with open(x, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    filtered_rows = [i for i in csv_reader if i[1] ==y] 

print(filtered_rows)