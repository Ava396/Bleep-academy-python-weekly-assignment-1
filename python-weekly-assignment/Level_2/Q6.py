# Q6. Write a function to check whether a number is prime.

def check_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if check_prime(number):
    print(number, "is a Prime Number.")
else:
    print(number, "is not a Prime Number.")