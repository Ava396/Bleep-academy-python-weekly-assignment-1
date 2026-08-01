# Q7. Write a function to calculate the GCD of two numbers.

def find_gcd(first_number, second_number):

    gcd = 1

    smaller = min(first_number, second_number)

    for i in range(1, smaller + 1):
        if first_number % i == 0 and second_number % i == 0:
            gcd = i

    return gcd


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", find_gcd(num1, num2))