# Q14. Sort a list in ascending order without using sort().

numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for i in range(n):
    for j in range(i + 1, n):

        if numbers[i] > numbers[j]:

            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Ascending Order:", numbers)




