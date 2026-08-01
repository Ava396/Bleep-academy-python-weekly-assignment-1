# Q5. Remove empty strings and strings containing only spaces.

words = ["Python", "", "Java", " ", "C++", "   ", "Django"]

result = [word for word in words if word.strip() != ""]

print("Original List:", words)
print("Updated List:", result)