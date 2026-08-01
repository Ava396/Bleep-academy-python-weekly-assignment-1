# Q10. Remove all spaces from a string and count the number of words.

text = input("Enter a sentence: ")

# Remove all spaces
no_spaces = text.replace(" ", "")

# Count words
words = text.split()
word_count = len(words)

print("\nSentence without spaces:", no_spaces)
print("Number of words:", word_count)