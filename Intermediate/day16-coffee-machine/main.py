from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#menu_item = MenuItem()
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_off = False
while not is_off:
    user_prompt = "What would you like? " + menu.get_items()
    user_input = input(user_prompt).lower()

    if user_input == "off":
        is_off = True
    elif user_input == "report":
        coffee_machine.report()
    else:
        menu_item = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_machine.make_coffee(menu_item)

