import random

heads_tails = random.randint(0,1)
if heads_tails == 1:
    print('Heads')
else:
    print('tails')

all_states_usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # Pick a random name from the list
names_string = ['Aaditya','Manav','Gaurab','Sushant','Mith','Aalok']
num_items = len(names_string)
random_choice = random.randint(0, num_items - 1)
person_to_pay = names_string[random_choice]
print(f'{person_to_pay} is going to pay for your food today!')
#
#
# #Treasure Map
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")

letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")

#RPS game
# Rock
rock = (
    ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""))

# Paper
paper = (
    ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""))

# Scissors
scissors = (
    ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""))
computer_play= [rock, paper, scissors]
random_choice = random.randint(0,2)
computer_choice = computer_play[random_choice]
user_input = int(input("What do want to choose? Type 0 for Rock, 1 for paper and 2 for Scissors.: "))
#when user = rock
if user_input == 0:
    print("You chose: ")
    print(rock)
    print(f"Computer choose: \n{computer_choice}")
    if user_input == 0 and random_choice == 1:
        print("You loose!")
    elif user_input == 0 and random_choice == 2:
        print("You win!")
    else:
        print("Draw!")
#when user = paper
if user_input == 1:
    print("You chose: ")
    print(paper)
    print(f"Computer choose: \n{computer_choice}")
    if user_input == 1 and random_choice == 0:
        print("You Win!")
    elif user_input == 1 and random_choice == 2:
        print("You Loose!")
    else:
        print("Draw!")
#when user = scisssors
if user_input == 2:
    print("You chose: ")
    print(scissors)
    print(f"Computer choose: \n{computer_choice}")
    if user_input == 2 and random_choice == 0:
        print("You loose!")
    elif user_input == 2 and random_choice == 1:
        print("You win!")
    else:
        print("Draw!")



