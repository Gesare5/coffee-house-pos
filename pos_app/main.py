from datetime import date
from coffee_craft_ops import craft_a_coffee, add_coffee_item



def prelim_list() -> list[str]:
    return [
        "A: Order Coffee",
        "B: Manage Coffee Items",
        "C: Exit",
    ]

def selection_list() -> list[str]:
    return [
        "1: Caffe Latte",
        "2: Vanilla Latte",
        "3: Cappuccino",
        "4: Espresso",
        "5: Mocha Latte",
    ]

def manage_coffee_items_list():
    return[
        "1: Add Coffee Item",
        "2: View Coffee Items"
    ]

def manage_coffee_items(choice):
    if int(choice) == 1:
        add_coffee_item()
    else:
        print(selection_list())

def handle_prelim_action(action):
    match action:
        case 'a':
            print("The available selection is:")
            for value in selection_list():
                print(value)
            coffee_choice = input()
            handle_selection(int(coffee_choice))    
        case 'b':
            print('.................')
            for value in manage_coffee_items_list():
                print(value)
            coffee_items_choice = input()
            manage_coffee_items(coffee_items_choice)
        case 'c':
            return
        

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

    while True:
        for value in prelim_list():
            print(value)
        prelim_action = input().lower()
        if prelim_action == 'c':
            break
        else:
            handle_prelim_action(prelim_action)

    

    


if __name__ == "__main__":
    main()
