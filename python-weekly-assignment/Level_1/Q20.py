# Q20. Rotate a list by K positions to the left.

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

k = int(input("Enter K: "))

for i in range(k):
    first = numbers[0]

    for j in range(n - 1):
        numbers[j] = numbers[j + 1]

    numbers[n - 1] = first

print("\nList after left rotation:", numbers)