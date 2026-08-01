# Q19. Separate even and odd numbers into two different lists.

numbers = []
even = []
odd = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("\nOriginal List:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

