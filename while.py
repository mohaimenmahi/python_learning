i = 0
secret = 9

while i < 3:
    guess = int(input("Guess: "))
    i = i + 1
    if secret == guess:
        print("You Win!")
        break
else:
    print("You Lose!")