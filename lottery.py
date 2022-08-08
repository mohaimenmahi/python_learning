import random

ids = []

start = 1000

for i in range(1000):
    ids.append(start)
    start += 1


number = int(input("Input the number: "))

k = 0

ans = []

while k < number:
    if k == number:
        break
    run = input("Run (press r for run, s for stop): ")
    if run.lower() == 'r':
        select = random.choice(ids)
        print(f"Id {select} is selected")
        ans.append(select)
        ids.remove(select)
    else:
        print("Lottery stopped")
    
    k += 1

ans.sort()

print("Selected Ids are: ", ans)