# Q12. Find the missing number from a list containing numbers from 1 to N.

numbers = []

n = int(input("Enter the value of N: "))

print("Enter", n - 1, "numbers:")

for i in range(n - 1):
    num = int(input("Enter number: "))
    numbers.append(num)

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing Number:", i)
    
    

