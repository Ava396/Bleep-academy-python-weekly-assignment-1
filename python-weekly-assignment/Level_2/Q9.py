# Q9. Write a function that accepts a sentence and returns the longest word.

def longest_word(sentence):

    words = sentence.split()

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input("Enter a sentence: ")

print("Longest Word:", longest_word(sentence))