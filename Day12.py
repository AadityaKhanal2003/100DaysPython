import random

print('''
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"                       
''')
print("Welcome to number guessing game.\nI'm thinking of a number between 1 and 100.")
difficulty_level = input('Type "easy" or "hard": ')
random_number = random.randint(1, 100)
guess_count = 10 if difficulty_level == 'easy' else 10
while guess_count > 0:
    def game(num_guessed):
        global guess_count
        if random_number == num_guessed:
            print("You've guessed it right.")
            guess_count = 0
        elif random_number != num_guessed:
            if num_guessed > random_number:
                print("Too high.")
                guess_count -= 1
                print(f"Looks like you've guessed it wrong. Guesses remaining: {guess_count}")
            elif num_guessed < random_number:
                print("Too Low.")
                guess_count -= 1
                print(f"Looks like you've guessed it wrong. Guesses remaining: {guess_count}")
            elif guess_count == 0:
                print(f'Correct answer: {random_number}')
        else:
            print('Invalid choice! ')

    if difficulty_level == 'easy':
        num_to_guess = int(input("Guess a number: "))
        game(num_to_guess)
    elif difficulty_level == 'hard':
        num_to_guess = int(input("Guess a number: "))
        game(num_to_guess)
    else:
        print('Error!')
