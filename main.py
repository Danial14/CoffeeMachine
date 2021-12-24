from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
continueMakingCoffee = True
coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()
def startMakingCoffee(userInput):
    menuIteM = menu.find_drink(userInput)
    if menuIteM:
        if coffeeMaker.is_resource_sufficient(menuIteM):
            if moneyMachine.make_payment(menuIteM.cost):
                coffeeMaker.make_coffee(menuIteM)

while continueMakingCoffee:
    userInput = input(f"What would you like? {menu.get_items()} : ").lower()
    if userInput == "off":
        continueMakingCoffee = False
    elif userInput == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        startMakingCoffee(userInput)


