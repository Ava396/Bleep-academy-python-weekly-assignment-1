# Q6. Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

text = input("Enter a string: ")

print("\nFirst 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Every alternate character:", text[::2])
print("Reversed string:", text[::-1])

