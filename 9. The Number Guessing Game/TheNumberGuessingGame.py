import random
import Beginner.Day12.art

easyLevel=10
hardLevel=5

def play():
    print(Beginner.Day12.art.logo)
    print("Welcome tot the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choose=input("Choose a difficulty. Type 'easy' or 'hard': ")
    number=random.randint(1,100)
    if choose == "easy":
        nrincercari=easyLevel
    else:
        nrincercari=hardLevel

    gnumber=-1
    while nrincercari>0:
        print(f"You have {nrincercari} attempts ramining to guess the number.")
        gnumber=int(input("Make a guess: "))
        if gnumber > number:
            print("Too high.")
            print("Guess again.")
            nrincercari -=1
        elif gnumber < number:
            print("Too low.")
            print("Guess again.")
            nrincercari -= 1
        else:
            print(f"You got it! The answer was {number}.")
            nrincercari=0

    if nrincercari == 0 and gnumber != number:
        print(f"You've run of guesses, you lose. The number was {number}")

play()