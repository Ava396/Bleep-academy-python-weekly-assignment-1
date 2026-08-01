# Q3. Find the largest and second largest among three numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

numbers = [num1, num2, num3]
numbers.sort(reverse=True)

print("\nLargest number:", numbers[0])
print("Second largest number:", numbers[1])