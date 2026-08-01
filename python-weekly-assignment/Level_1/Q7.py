# Q7. Count vowels, consonants, digits, and special characters.

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("\n----- Result -----")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)

