# Q13. Find the frequency of each element in a list.

frequency = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    frequency.append(num)

printed = []

for item in frequency:

    if item not in printed:

        count = frequency.count(item)

        print(item, "appears", count, "times")

        printed.append(item)