import Day14Data
import random

# display 2 details to compare to a user
# keep the one with higher follower and randomly pick another
# stop if the user guesses lower than expected
# add a try again feature if the game ends.

A = random.randint(0, 50)
B = random.randint(0,50)
print(f"Compare A: {Day14Data.data[A]['name']}, a {Day14Data.data[A]['description']} from {Day14Data.data[A]['country']}")
print(f"Compare B: {Day14Data.data[B]['name']}, a {Day14Data.data[B]['description']} from {Day14Data.data[B]['country']}")

player_choice = input("Who has more followers? Type 'A' or 'B': ")
game_continue = True
while game_continue:
    if player_choice == "A" and (Day14Data.data[A]['follower_count']>Day14Data.data[B]['follower_count']):
        print(f"{Day14Data.data[A]['name']} has more followers")
        print("---------------------------------------------------------------------------------------------")
        B = random.randint(0, 50)
        print(f"Compare A: {Day14Data.data[A]['name']}, a {Day14Data.data[A]['description']} from {Day14Data.data[A]['country']}")
        print(f"Compare B: {Day14Data.data[B]['name']}, a {Day14Data.data[B]['description']} from {Day14Data.data[B]['country']}")
        player_choice = input("Who has more followers? Type 'A' or 'B': ")
    elif player_choice == "B" and (Day14Data.data[B]['follower_count'] > Day14Data.data[A]['follower_count']):
        print(f"{Day14Data.data[B]['name']} has more followers.")
        print("---------------------------------------------------------------------------------------------")
        A = random.randint(0, 50)
        print(f"Compare A: {Day14Data.data[B]['name']}, a {Day14Data.data[B]['description']} from {Day14Data.data[B]['country']}")
        print(f"Compare B: {Day14Data.data[A]['name']}, a {Day14Data.data[A]['description']} from {Day14Data.data[A]['country']}")
        player_choice = input("Who has more followers? Type 'A' or 'B': ")
    else:
        play_again = input(f"Sorry, Game is over. Would you like to play to play again? (Y/N): ").lower()
        if play_again == 'y':
            A = random.randint(0, 50)
            B = random.randint(0, 50)
            print(f"Compare A: {Day14Data.data[A]['name']}, a {Day14Data.data[A]['description']} from {Day14Data.data[A]['country']}")
            print(f"Compare B: {Day14Data.data[B]['name']}, a {Day14Data.data[B]['description']} from {Day14Data.data[B]['country']}")
            player_choice = input("Who has more followers? Type 'A' or 'B': ")
        else:
            print("Thank You! The game is now closed.")
            break