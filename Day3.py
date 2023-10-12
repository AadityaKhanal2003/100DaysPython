# odd or even
user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print('even')
else:
    print('odd')

#Ticket price calculator
height_input = int(input("Enter your height: "))
total_bill = 0
if height_input > 120:
    print('can ride')
    age = int(input('Enter your age: '))
    if age >= 18:
        total_bill += 12
    elif 45 <= age <= 55:
        total_bill += 0
        print('your total is',total_bill)
    elif 12 < age < 18:
        total_bill += 7
    else:
        total_bill += 5
    want_photo = input('Do you want photos? (y/n): ')
    if want_photo == 'y':
        total_bill += 3
        print(f'Your total bill is: ${total_bill}')
    else:
        print(f'Your total bill is ${total_bill}')
else:
    print('cant ride')

# #BMI 2.0
height = float(input("Enter your height: "))
weight = int(input("Enter you weight: "))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print(f' Your BMI: {BMI}, underweight.')
elif BMI < 25:
    print(f' Your BMI: {BMI}, normal weight.')
elif BMI > 30:
    print(f' Your BMI: {BMI} , slightly over weight.')
elif BMI < 35:
    print(f' Your BMI: {BMI} , you are fat.')
else:
    print(f' Your BMI: {BMI}, clinically obese.')

# # #leap-year
input_year = int(input("Enter any year: "))
if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
         print('leap year')
else:
    print('Not leap year')

print('Thank you for choosing python deliveries. ')
size_pizza = input('What pizza do you want? ')
add_pepperoni = input("Do you want to add pepperoni? Y/N ")
extra_Cheese = input("Do you want to add extra cheese? Y/N ")
total_bill = 0
# #for small pizza
if size_pizza == 'S':
    total_bill += 4.99
    if add_pepperoni == 'Y':
        total_bill += 2.0
    if extra_Cheese == 'Y':
        total_bill += 1.29
        print(f'Yor total is {total_bill}')
    else:
        print(f'Yor total is {total_bill}')
# #for medium pizza
elif size_pizza == 'M':
    total_bill += 12.99
    if add_pepperoni == 'Y':
        total_bill += 3.0
    if extra_Cheese == 'Y':
        total_bill += 1.29
        print(f'Yor total is {total_bill}')
    else:
        print(f'Yor total is {total_bill}')
# #for large pizza
elif size_pizza == 'L':
    total_bill += 24.99
    if add_pepperoni == 'Y':
        total_bill += 3.0
    if extra_Cheese == 'Y':
        total_bill += 1.29
        print(f'Yor total is {total_bill}')
    else:
        print(f'Yor total is {total_bill}')
else:
    print(f'Your total bill is: {total_bill}')

#Love Calulator
print('Welcome to Love Calculator!!! ')
partner_1 = input("Enter your name: ")
partner_2 = input("Enter your name: ")
merged_name = partner_1+partner_2
lower_name = merged_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = t + r + u + e
score = int(str(first_digit) + str(second_digit))
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif (score >= 40) and (score <= 50):
    print(f"Your love score: {score}, you're alright together.")
else:
    print(f'You\'re score is {score}.')

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
print('To start the game, Choose an option L for left or R for right')
gamer_choice = input("Enter L or R: ").lower()
if gamer_choice == "l":
    print('You\'ve now come to the lake')
    gamer_choice2 = input("Enter S to swim and W to wait.").lower()
    if gamer_choice2 == 'w':
        print('You survived crossing the lake, Now you\'re in front of a door.')
        gamer_choice3 = input("What door do you want to choose? Red, Blue or Yellow.").lower()
        if gamer_choice3 == 'yellow':
            print('You are a winner !!!')
        elif gamer_choice3 == 'red':
             print('Oop! room full of snakes.')
        elif gamer_choice3 == 'blue':
             print('Oop! You fell into a pit full of cockroaches.')
        else:
            print('Good game for reaching uptill here, you were one step closer.')
    else:
        print('Oops! Crocodiles were hungry.')
else:
    print('You died because of an accident, Game over.')

