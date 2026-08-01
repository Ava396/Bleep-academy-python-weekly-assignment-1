# Q2. Generate the Fibonacci sequence using recursion.

def fibonacci(number):

    if number == 0:
        return 0

    elif number == 1:
        return 1

    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


n = int(input("Enter the number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")