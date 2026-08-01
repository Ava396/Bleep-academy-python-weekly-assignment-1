# Q9. Find the frequency of each character in a string.

text = input("Enter a string: ")
frequency = ""
for char in text:
    count = text.count(char)
    print(char , ":" ,count)
    frequency += char