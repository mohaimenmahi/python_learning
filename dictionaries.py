customer = {
    "name": "Jhon Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("status"))
print(customer.get("status", "Passed"))
print(customer) # {'name': 'Jhon Smith', 'age': 30, 'is_verified': True}
customer["name"] = "Jack"
print(customer)
customer["status"] = "Passed"
print(customer) # {'name': 'Jack', 'age': 30, 'is_verified': True, 'status': 'Passed'}

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = input("Phone: ")

output = ""

for item in phone:
    output += numbers[item] + " "

print(output)