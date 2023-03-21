from logo import logo
import random

print(logo)

def welcome(chosenNumber):
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100.")

    print("(spoiler) Answer is ", chosenNumber)
    print("Choose difficulty. Type 'easy' or 'hard': ")

def random_num():
    return random.randint(1,100)

def guessing_number(ChosenNumber, numberOfTries):
    while numberOfTries > 0:
        guess = input("Make a guess: ")
        guess = int(guess)

        if guess == ChosenNumber:
            print("You win, the answer is ", ChosenNumber)
            break
        elif guess < chosenNumber:
            print("Too low")
            numberOfTries -= 1
            if numberOfTries > 0:
                print ("Guess again")
                print("You have ", numberOfTries, "attempts remaining")
        elif guess > chosenNumber:
            print("Too high, guess again")
            numberOfTries -= 1
            if numberOfTries > 0:
                print("Guess again")
                print("You have ", numberOfTries, "attempts remaining")
    
    if numberOfTries == 0:
        print("You've run out of guesses, you lose.")


numberOfTries = 0
chosenNumber = random_num()

welcome(chosenNumber)

while True:
    level = input()
    if level == 'easy':
        numberOfTries = 10
        print("You have", numberOfTries, "attempts to guess the number")
        break
    elif level == 'hard':
        numberOfTries = 5
        print("You have", numberOfTries, "attempts to guess the number")
        break
    else:
        print("Wrong word, try again")

guessing_number(chosenNumber, numberOfTries)