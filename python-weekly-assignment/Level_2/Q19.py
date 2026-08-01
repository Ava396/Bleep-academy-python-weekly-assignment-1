# Q19. Handle FileNotFoundError while opening a file.

try:

    file = open("data.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("File not found.")