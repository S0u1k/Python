# Program to check which character is present at which index

# Take input from user
text = input("Enter a string: ")

# Loop through the string using enumerate
for index, char in enumerate(text):
    print(f"Character '{char}' is at index {index}")
