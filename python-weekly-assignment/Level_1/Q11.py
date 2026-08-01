# Q11. Print all prime numbers between 1 and N.

number = int(input("Enter a number: "))

print("\nPrime numbers between 1 and", number, "are:")

for i in range(2, number + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)