import csv
# Writing to a CSV file
#f = "E:/xiics1st2024-25/College 25-26/Python/17.8.25/"
data = [
    ['Name', 'Age', 'Address'],
    ['Rupanjan Jalimal', 18, 'Kestopur'],
    ['Souvik Tuklibaj', 18, 'New Town'],
    ['Arisha Malkhor Matal', 18, 'Baguiati']
]
print(data)
x=input("Enter the File name = ")
with open(x, mode='w', newline='') as file:
    p = csv.writer(file)
    p.writerows(data)
print("File created Successfully!!!!")