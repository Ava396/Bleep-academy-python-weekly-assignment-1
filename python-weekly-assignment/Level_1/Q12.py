# Q12. Generate the Fibonacci sequence up to N terms.

terms = int(input("Enter the number of terms: "))

first = 0
second = 1

print("\nFibonacci Sequence:")

for i in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number