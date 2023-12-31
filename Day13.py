# Debugging
def myFunction():
    for i in range(0,20+1):
        if i == 20:
            print('You\'ve got this')
myFunction()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5 )
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year >= 1980 and year <= 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])