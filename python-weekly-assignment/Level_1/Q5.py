# Q5. Check whether a number is an Armstrong number.

number = int(input("Enter a number: "))

original_number = number
sum = 0

digits = len(str(number))

while number > 0:
    digit = number % 10
    sum = sum + digit ** digits
    number = number // 10

if sum == original_number:
    print(original_number, "is an Armstrong number.")
else:
    print(original_number, "is not an Armstrong number.")