import random
import os

clear = lambda: os.system('cls')
clear()
number = random.randint(1,100)
print("Welcome to number guessing game.")
print("I'm guessing a number between 1 and 100")

difficulty = input("choose a difficulty: 'easy' or 'hard'").lower()

if difficulty == 'easy':
    chances = 10
else: 
    chances = 5

while chances > 0:
    print(f"You have {chances} attempts remaining")
    guess = int(input('Make a Guess: '))
    if guess > number:
        print("Too High \n")
        chances -= 1
    elif guess < number:
        print("Too LOW \n")
        chances -= 1
    elif guess == number:
        print(f"You got the number. The number was {number}")
        exit()
    
print("You are out of chances! You Lost")
print(f"The number was {number}")
