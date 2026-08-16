# CODOMAX Internship - Module 2
# Project 2: Number Guessing Game
# Difficulty: Medium

import random
 
def guessing_game():
    print("=== Number Guessing Game ===")
    number = random.randint(1, 100)
    attempts = 7
    guessed = False
 
    print(f"Guess a number between 1 and 100. You have {attempts} attempts.")
 
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
 
        if guess == number:
            print(f"Correct! You guessed it in {attempt} attempt(s).")
            guessed = True
            break
        elif guess < number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")
 
    if not guessed:
        print(f"Out of attempts! The correct number was {number}.")
 
 
if __name__ == "__main__":
    guessing_game()
 