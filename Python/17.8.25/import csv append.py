import csv
# Appending to a CSV file
new_data = [
    ['Aritra', '18', 'Chingrighata'],
    ['Pranab', '36', 'kestopur'],
    ['Dip','31','Salt lake'],
    ['Randhir','18','Kestopur']
]
x=input("Enter the File Name = ")
with open(x, mode='a', newline='') as file:
    add = csv.writer(file)
    add.writerows(new_data)
print("File Updated Successfully!!!")
with open(x, mode='r') as file:
    a = csv.reader(file)
    for i in a:
        print(i)