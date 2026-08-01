# Q18. Find the second largest and second smallest element in a list.

result = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    number = int(input("Enter number: "))
    result.append(number)

result.sort()

print("Second Smallest Element:", result[1])
print("Second Largest Element:", result[-2])


