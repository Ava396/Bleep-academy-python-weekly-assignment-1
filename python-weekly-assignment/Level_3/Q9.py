# Q9. Flatten a nested list using recursion.

def flatten(data):

    result = []

    for item in data:

        if isinstance(item, list):

            result.extend(flatten(item))

        else:

            result.append(item)

    return result


numbers = [1, [2, 3], [4, [5, 6]], 7]

print("Original List:", numbers)

print("Flattened List:", flatten(numbers))