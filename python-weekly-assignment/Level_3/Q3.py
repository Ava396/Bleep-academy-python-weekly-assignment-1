# Q3. Find the sum of digits of a number using recursion.

def sum_digits(number):

    if number == 0:
        return 0

    return number % 10 + sum_digits(number // 10)


number = int(input("Enter a number: "))

print("Sum of Digits:", sum_digits(number))