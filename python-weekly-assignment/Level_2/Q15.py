# 15. Print a diamond star pattern.

n = int(input("Enter number of rows: "))

# Upper Part
for i in range(1, n + 1):

    print(" " * (n - i), end="")

    print("*" * (2 * i - 1))

# Lower Part
for i in range(n - 1, 0, -1):

    print(" " * (n - i), end="")

    print("*" * (2 * i - 1))