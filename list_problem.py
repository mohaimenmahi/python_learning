numbers = [20, 15, 1, 9, 522, 11, 86, 654, 222]

max_num = numbers[0]

for item in numbers:
    if max_num < item:
        max_num = item

print(max_num)