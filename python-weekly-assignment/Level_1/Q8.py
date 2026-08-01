# Q8. Check whether a string is a palindrome using slicing.

text = input("Enter a string: ")

if text == text[::-1]:
    print(text, "is a Palindrome.")
else:
    print(text, "is not a Palindrome.")