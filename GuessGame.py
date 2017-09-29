# This is a small python roulette game

import random

machineGuess = random.randint(0,81)

while True:
    humanGuess = int(input("Enter the number between 0-81: "))
    if humanGuess > machineGuess:
        print("Enter the lower value")
    elif humanGuess < machineGuess:
        print("Enter the higher value")
    else:
        print("Hooray..! You've got the right number.")
        break
    



