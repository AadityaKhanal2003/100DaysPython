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
guess_count_hard = 5
guess_count_easy = 10
while True:
    def easy_level(num_guessed, g_c):
        if random_number == num_guessed:
            print("You've guessed it right.")
        elif random_number != num_guessed:
            g_c -= 1
            print(f"Looks like you've guessed it wrong. Guesses remaining: {g_c}")
        else:
            print('Invalid Input.')


    def hard_level(num_guessed, g_c):
        if random_number == num_guessed:
            print("You've guessed it right.")
        elif random_number != num_guessed:
            g_c -= 1
            print(f"Looks like you've guessed it wrong. Guesses remaining: {g_c}")
        else:
            print('Invalid Input.')


    if difficulty_level == 'easy':
        user_req = int(input("Guess the number: "))
        easy_level(user_req, guess_count_easy)
    elif difficulty_level == 'hard':
        user_req = int(input("Guess the number: "))
        hard_level(user_req, guess_count_hard)
    else:
        print('Error!')
