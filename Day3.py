#odd or even

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

#BMI 2.0
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
    print(f' Your BMI: {BMI} , you are fat..')
else:
    print(f' Your BMI: {BMI}, clinically obese.')

# #leap-year
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


