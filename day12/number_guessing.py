#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
def difficulty_level(word):
    if word == "easy":
        return 10
    elif word == "hard":
        return 5
    else:
        return 0
# from art import logo
# print(logo)

def game():
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    correct_number = random.randint(1, 101)
    print(f"The correct number is {correct_number} ")
    word = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    input_word = difficulty_level(word)
    
    end_game = False
    while not end_game:
        print(f"You have {input_word} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == correct_number :
            end_game = True
            print(f"You got it the answer is {correct_number}")
        elif guess < correct_number :
            input_word -= 1
            print("Too low")
            if input_word == 0 :
                end_game = True
                print("You've run out of guesses, you lose")
                return
        elif guess > correct_number :
            input_word -= 1
            print("Too high.")
            if input_word == 0 :
                end_game = True
                print("You've run out of guesses, you lose")
                return
        else:
            end_game = True

game()