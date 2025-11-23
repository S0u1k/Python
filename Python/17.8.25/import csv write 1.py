import csv
# Writing to a CSV file
li = []
heading=['Roll No.','Name','Age','DSA']
r = int(input("Enter number of rows: "))
for i in range(0,r,1):#1
  row = []
  for j in range(0,4,1):
    row.append(input(f"Enter the {heading[j]}: "))
  li.append(row)
  #print(row)
#print(li)
x=input("Enter the File name = ")
with open(x, mode='w', newline='\n') as file:
    data_x = csv.writer(file)
    data_x.writerow(heading)
    data_x.writerows(li)