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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_status = True

# Coins
QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

# Costs for Coffees
COST_ESPRESSO = 1.50
COST_LATTE = 2.50
COST_CAPPUCCINO = 3.00


def check_user_input(user_choice):
    # TODO 2. Turn off the coffee machine by entering 'off' to the prompt.
    if user_choice == 'off':
        global coffee_machine_status
        coffee_machine_status = False
    elif user_choice == 'report':
        show_report()
    elif user_choice == 'espresso':
        make_espresso()
    elif user_choice == 'latte':
        make_latte()
    elif user_choice == 'cappuccino':
        make_cappuccino()


# TODO 3. Print report
def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO 4. Check resources sufficient?
def check_resources_sufficient(available_resource, user_choice):
    if user_choice == 'espresso':
        if available_resource['water'] >= 50 and available_resource['coffee'] >= 18:
            return True
        elif available_resource['water'] < 50:
            print("Sorry there is not enough water.")
            return False
        elif available_resource['coffee'] < 18:
            print("Sorry there is not enough coffee.")
            return False
    elif user_choice == 'latte':
        if available_resource['water'] >= 200 and available_resource['coffee'] >= 24 and available_resource['milk'] >= 150:
            return True
        elif available_resource['water'] < 200:
            print("Sorry there is not enough water.")
            return False
        elif available_resource['coffee'] < 24:
            print("Sorry there is not enough coffee.")
            return False
        elif available_resource['milk'] < 150:
            print("Sorry there is not enough milk.")
            return False
    elif user_choice == 'cappuccino':
        if available_resource['water'] >= 250 and available_resource['coffee'] >= 24 and available_resource['milk'] >= 100:
            return True
        elif available_resource['water'] < 250:
            print("Sorry there is not enough water.")
            return False
        elif available_resource['coffee'] < 24:
            print("Sorry there is not enough coffee.")
            return False
        elif available_resource['milk'] < 100:
            print("Sorry there is not enough milk.")
            return False


# TODO 5. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters, dimes, nickles, pennies


# TODO 6. Check transaction successful?
def check_transaction_successful(quarter, dime, nickle, penny, user_choice):
    user_payed = quarter * QUARTER + dime * DIME + nickle * NICKLE + penny * PENNY
    global profit
    if user_choice == 'espresso':
        profit = profit + COST_ESPRESSO
        if user_payed >= COST_ESPRESSO:
            change = user_payed - COST_ESPRESSO
            return change
        else:
            print("Sorry that's not enough money. Money refunded.")
    if user_choice == 'latte':
        profit = profit + COST_LATTE
        if user_payed >= COST_LATTE:
            change = user_payed - COST_LATTE
            return change
        else:
            print("Sorry that's not enough money. Money refunded.")
    if user_choice == 'cappuccino':
        profit = profit + COST_CAPPUCCINO
        if user_payed >= COST_CAPPUCCINO:
            change = user_payed - COST_CAPPUCCINO
            return change
        else:
            print("Sorry that's not enough money. Money refunded.")


def deduct_resource(water, coffee, milk):
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['milk'] -= milk


# TODO 7. Make Coffee
def make_espresso():
    has_resource = check_resources_sufficient(resources, user_input)
    if has_resource:
        quarter, dime, nickle, penny = process_coins()
        change = check_transaction_successful(quarter, dime, nickle, penny, user_input)
        deduct_resource(50, 18, 0)
        print(f"Here is ${round(change, 2)} in change.")
        print("Here is your espresso ☕. Enjoy!")


def make_latte():
    has_resource = check_resources_sufficient(resources, user_input)
    if has_resource:
        quarter, dime, nickle, penny = process_coins()
        change = check_transaction_successful(quarter, dime, nickle, penny, user_input)
        deduct_resource(200, 24, 150)
        print(f"Here is ${round(change, 2)} in change.")
        print("Here is your latte ☕. Enjoy!")


def make_cappuccino():
    has_resource = check_resources_sufficient(resources, user_input)
    if has_resource:
        quarter, dime, nickle, penny = process_coins()
        change = check_transaction_successful(quarter, dime, nickle, penny, user_input)
        deduct_resource(250, 24, 100)
        print(f"Here is ${round(change, 2)} in change.")
        print("Here is your cappuccino ☕. Enjoy!")


# Driver Code
while coffee_machine_status:
    # TODO 1. Prompt user by asking "What would you like?"
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    check_user_input(user_input)