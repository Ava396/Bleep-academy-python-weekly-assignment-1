# Q11. Find the common elements between two lists without using sets.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common)