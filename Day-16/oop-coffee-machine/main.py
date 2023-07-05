from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    options = Menu().get_items()
    customer_choice = input(f"What would you like? {options}: ")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        drink = Menu().find_drink(customer_choice)

        if CoffeeMaker().is_resource_sufficient(drink) and MoneyMachine().make_payment(drink.cost):
            CoffeeMaker().make_coffee(drink)
