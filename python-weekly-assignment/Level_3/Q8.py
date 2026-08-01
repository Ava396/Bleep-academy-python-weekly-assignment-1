# Q8. Read numbers until "stop" is entered.

numbers = []

while True:

    value = input("Enter number (or stop): ")

    if value.lower() == "stop":
        break

    try:
        numbers.append(float(value))

    except ValueError:
        print("Invalid input!")

numbers.sort()

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Average:", sum(numbers) / len(numbers))

length = len(numbers)

if length % 2 == 0:

    median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2

else:

    median = numbers[length // 2]

print("Median:", median)