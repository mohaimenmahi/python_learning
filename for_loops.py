##for item in range(10):
##    print(item)

##for item in range(5, 10):
##    print(item)

## for item in range(5, 10, 2):
##    print(item)

numbers = [5, 2, 5, 2, 2]

for value in numbers:
    str = ''
    for item in range(value):
        str += 'x'
    print(str)
    