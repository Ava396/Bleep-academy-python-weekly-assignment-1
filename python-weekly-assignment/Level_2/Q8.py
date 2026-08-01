# Q8. Write a function that returns the second largest element of a list.

def second_largest(numbers):

    numbers.sort()

    return numbers[-2]


numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Second Largest Element:", second_largest(numbers))