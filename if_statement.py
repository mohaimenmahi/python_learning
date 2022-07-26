price = 10 ** 6

buyer_credit = input("Buyer Credit(G/B): ")

if buyer_credit == 'G':
    price = price * 0.1
else:
    price = price * 0.2

print(f"Down Payment: {price}")