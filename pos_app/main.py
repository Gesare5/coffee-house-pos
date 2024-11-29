from datetime import date
from coffee_craft_ops import craft_a_coffee


def selection_list() -> list[str]:
    return [
        "1: Caffe Latte",
        "2: Vanilla Latte",
        "3: Cappuccino",
        "4: Espresso",
        "5: Mocha Latte",
    ]

def handle_selection(choice):
    choice_list = str.split(selection_list()[choice-1])
    coffe_choice = " ".join([choice_list[1], choice_list[2]]).lower()
    craft_a_coffee(coffe_choice)
    return

def main():
    print("Good day!")
    print("Date", date.today())
    print("Welcome to TeleBaristas!")
    print("")
    print("The available selection is:")

    for value in selection_list():
        print(value)

    coffee_choice = input()
    handle_selection(int(coffee_choice))


main()
