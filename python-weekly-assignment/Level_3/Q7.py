# Q7. Create a list containing only prime numbers.

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime Numbers:", prime_numbers)