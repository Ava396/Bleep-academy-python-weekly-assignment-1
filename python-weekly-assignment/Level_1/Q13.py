# Q13. Find all factors of a given number.

number = int(input("Enter a number: "))

print("\nFactors of", number, "are:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)