# Q14. Check whether a number is a Perfect Number.

number = int(input("Enter a number: "))

sum_of_factors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_factors += i

if sum_of_factors == number:
    print(number, "is a Perfect Number.")
else:
    print(number, "is not a Perfect Number.")