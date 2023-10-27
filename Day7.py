#Hangman Project
import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
''')
hangman_figure = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
all_words = ["Interstellar", "Avatar", "Inception", "JurassicPark", "Gladiator", "lasagna", "sushi", "chocolate", "hamburger", "pineapple", "telescope", "computer", "telephone", "guitar", "binoculars", "elephant", "kangaroo", "octopus", "flamingo", "crocodile"]
dashes_list = []
game_complete = False
total_lives = 6
stages_count = len(hangman_figure)
random_word = random.choice(all_words)
random_word = random_word.strip().lower()
word_len = len(random_word)

dash_count = len(random_word)
for a in range(dash_count):
    dashes_list.append("_")
print(dashes_list)
while not game_complete:
    guess_letter = input("Guess a letter: ").lower()
    for position in range(word_len):
        letter = random_word[position]
        if letter == guess_letter:
            dashes_list[position] = letter
    if guess_letter not in random_word:
        total_lives -= 1
        print(hangman_figure[stages_count-1])
        stages_count -= 1
        if total_lives == 0:
            game_complete = True
            print(hangman_figure[0])
    print(dashes_list)
    if "_" not in dashes_list:
        game_complete = True
        print("You saved the man from dying. Congratulations!")