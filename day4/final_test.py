rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

numbers = [rock, paper, scissors]

game = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(numbers[game])
  
print("Computer chose: ")
  
game_number = random.randint(0, 2)
print(numbers[game_number])



if game == 0 and game_number == 1 :
  print("You lose")
elif game == 1 and game_number == 0 :
  print("You win")
elif game == 0 and game_number == 0 :
  print("Its a draw")
elif game == 1 and game_number == 1 :
  print("Its a draw")
elif game == 2 and game_number == 0 :
  print("You lose")
elif game == 0 and game_number == 2 :
  print("You win")
elif game == 2 and game_number == 2 :
  print("its a Draw")
elif game == 1 and game_number == 2 :
  print("You lose")
elif game == 2 and game_number == 1 :
  print("You win")
  
  



