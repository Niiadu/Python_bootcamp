from art_game import logo
from art_game import vs
from game_data import data
import random
# import clear

rand = random.randrange(0, len(data))
lives = 0
random_data = data[rand]
print(logo)
compare_a = print(f"Compare A: {random_data['name']}, a {random_data['description']}, from {random_data['country']}.")
count_a = random_data['follower_count']

end_game = False
while not end_game:
    second_random = random.randrange(0, len(data))
    
    second_data = data[second_random]

    count_b = second_data['follower_count']

    a = count_a
    b = count_b
    print(vs)
    compare_b = print(f"Compare B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}.")
    followers = input("Who has more followers. 'A' or 'B': ").lower()

    if followers == "a":
        if a > b :
            # clear()
            print(logo)
            lives += 1
            print(f"You're right! your current score: {lives}.")
            compare_a = print(f"Compare A: {second_data['name']}, a {second_data['description']}, from {second_data['country']}.")
            count_a = second_data['follower_count']
        else:
            end_game = True
            # clear()
            print(f"Sorry, that's wrong. Final score: {lives}")
            
    elif followers == "b" :
        if b > a :
            # clear
            print(logo)
            lives += 1
            print(f"You're right! your current score: {lives}.")
            compare_a = print(f"Compare A: {second_data['name']}, a {second_data['description']}, from {second_data['country']}.")
            count_a = second_data['follower_count']
        else:
            end_game = True
            # clear()
            print(f"Sorry, that's wrong. Final score: {lives}")
            
    

