MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
resources = {
    'water': 600,
    'milk': 400,
    'coffee': 300
}


def ask_for_money():
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01
    return total


def sufficient_resource(order_ingredients):
    for item in order_ingredients:
        if resources[item] > order_ingredients[item]:
            return True
        else:
            print("Sorry, out of ingredients! Please come back later. ")
            False


def transaction_process(money_received, drink_price):
    if money_received >= drink_price:
        change_amount = round(money_received - drink_price)
        print(f"Your change is ${change_amount}.")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry, you don't have enough money. Refunding ....")
        return False


def make_coffee(coffee_types, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {coffee_types} ☕ ready")


is_on = True
while is_on:
    customerInput = input("What would you like? (espresso, latte, cappuccino))").lower()
    if customerInput == 'off':
        is_on = False
    elif customerInput == 'report':
        print(f'Coffe: {resources["coffee"]}g.')
        print(f'Water: {resources["water"]}ml.')
        print(f'Milk: {resources["milk"]}ml.')
        print(f'Profit: ${profit}.')
    else:
        coffee_type = MENU[customerInput]
        if sufficient_resource(coffee_type["ingredients"]):
            payment = ask_for_money()
            if transaction_process(payment, coffee_type['cost']):
                make_coffee(customerInput, coffee_type['ingredients'])
