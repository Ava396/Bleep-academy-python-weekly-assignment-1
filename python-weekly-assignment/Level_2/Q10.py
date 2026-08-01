# Q10. Write a function that merges two lists and removes duplicate elements.

def merge(list1, list2):

    merged_list = list1 + list2

    unique = []

    for item in merged_list:
        if item not in unique:
            unique.append(item)

    return unique


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = merge(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", result)