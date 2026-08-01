# Q17. Accept integer input until a valid integer is entered.

while True:

    try:
        number = int(input("Enter an integer: "))

        print("You entered:", number)

        break

    except ValueError:
        print("Invalid input! Please enter an integer.")