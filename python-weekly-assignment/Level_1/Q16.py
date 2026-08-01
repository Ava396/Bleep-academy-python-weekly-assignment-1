# Q16. Find the largest, smallest, and average value in a list.

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print("\nList:", numbers)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Average:", average)