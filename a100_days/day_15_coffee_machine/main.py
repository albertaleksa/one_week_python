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

money_profit = 0


# TODO: 1. Print report
def print_report():
    """Print report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_profit}")


# TODO: 2. Check resources sufficient?
def check_resources(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. Process coins
def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters_count = int(input("how many quarters?: "))
    dimes_count = int(input("how many dimes?: "))
    nickles_count = int(input("how many nickles?: "))
    pennies_count = int(input("how many pennies?: "))
    total = 0.25 * quarters_count + 0.10 * dimes_count + 0.05 * nickles_count + 0.01 * pennies_count
    return total


# TODO: 4. Check transaction successful?
def check_transaction(drink_cost, money):
    """Return True when payment is accepted, False if money is insufficient."""
    if money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global money_profit
        money_profit += drink_cost
        if money > drink_cost:
            change = round(money - drink_cost, 2)
            print(f"Here is ${change} in change.")
        return True


# TODO: 5. Make Coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def start():
    while True:
        user_input = input("​What would you like? (espresso/latte/cappuccino): ​")
        if user_input == "report":
            print_report()
        elif user_input == "off":
            break
        elif user_input in ("espresso", "latte", "cappuccino"):
            drink = MENU[user_input]
            if check_resources(drink["ingredients"]):
                inserted_coins = process_coins()
                if check_transaction(drink["cost"], inserted_coins):
                    make_coffee(user_input, drink["ingredients"])
        else:
            print("I don't know this command!")


if __name__ == "__main__":
    start()
