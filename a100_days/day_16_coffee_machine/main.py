from a100_days.day_16_coffee_machine.menu import Menu, MenuItem
from a100_days.day_16_coffee_machine.coffee_maker import CoffeeMaker
from a100_days.day_16_coffee_machine.money_machine import MoneyMachine

if __name__ == "__main__":
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    while True:
        user_input = input(f"​What would you like? ({menu.get_items()}): ​")
        if user_input == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_input == "off":
            break
        elif user_input in ("espresso", "latte", "cappuccino"):
            drink = menu.find_drink(user_input)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("I don't know this command!")