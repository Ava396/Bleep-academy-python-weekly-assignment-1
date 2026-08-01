# Q17. Remove duplicate elements from a list.

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter the number of elements: "))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
         unique_numbers.append(num)

print("\nOriginal List:", numbers)
print("List after removing duplicates:", unique_numbers)