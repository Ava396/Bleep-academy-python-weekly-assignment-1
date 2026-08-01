# Q4. Create a list containing the lengths of each word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

lengths = [len(word) for word in words]

print("Word Lengths:", lengths)