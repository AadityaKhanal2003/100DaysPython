# BMI calculator
height = float(input("Enter your height: "))
weight = int(input("Enter you weight: "))
BMI  = weight / (height ** 2)
print(f'BMI is %.2f'% BMI)

#Tip Calculator:

print("Welcome to Tip calculator! ")
user_input = float(input("what was the total bill: "))
tip_query = int(input("how much tip would you like to give? 10, 12, 15: "))
split_amt_query = int(input("How many people do you want to split the amount with?: "))

total_amt = (user_input + (user_input * (tip_query/100))) / split_amt_query
print('Each person should pay: ${:.2f}'.format(total_amt))

