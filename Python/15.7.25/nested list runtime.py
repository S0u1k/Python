nested_list = []
n = int(input("How many sub-lists? "))

for i in range(n):
    sub_list = int(input(f"Enter elements of sub-list {i+1} (separated by space): ")).split()
    nested_list.append(sub_list)

print("Nested List:", nested_list)