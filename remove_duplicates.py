numbers = [5, 2, 9, 8, 7, 5, 8]
unique = []

for item in numbers:
    if item not in unique:
        unique.append(item)

print(unique)