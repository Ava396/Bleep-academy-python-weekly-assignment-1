# Q18. Handle IndexError while accessing list elements.

numbers = [10, 20, 30, 40]

try:

    index = int(input("Enter index: "))

    print("Element:", numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter a valid integer.")