import random
import math
number = random.randint(1, 50)
attempts = 5
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50")
print("You have 5 attempts.\n")
for i in range(attempts):
    guess = int(input("Enter your guess: "))
    difference = math.fabs(number - guess)
    if guess == number:
        print(" Congratulations! You guessed the correct number!")
        break
    else:
        print(f"Wrong guess! You are {difference} away from the correct number.")
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
    print(f"Attempts left: {attempts - i - 1}\n")
else:
    print("\n You've used all attempts!")
    print(f"The correct number was: {number}")
