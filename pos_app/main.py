from datetime import date
from coffee_craft_ops import generate_coffee_list, generate_coffee_table_list, craft_a_coffee, manage_coffee_items
from utils import generate_table


COFFEE_SELECTION_LIST = generate_coffee_list()
COFFEE_TABLE_SELECTION_LIST = generate_coffee_table_list()


def prelim_list() -> list[str]:
    return [
        "A: Order Coffee",
        "B: Manage Coffee Items",
        "C: Exit",
    ]

def manage_coffee_items_list():
    return[
        ['1',"Add Coffee Item"],
        ['2',"Delete Coffee Item"],
        ['3',"View Coffee Items"]
    ]

def handle_prelim_action(action):
    match action:
        case 'a':
            print('')
            generate_table(
                COFFEE_TABLE_SELECTION_LIST, 
                ['Choice', 'Coffee'], 
                'bright_green', 
                'Coffee List'
                )
            coffee_choice = input()
            handle_selection(int(coffee_choice))    
            print('')

        case 'b':
            print('')
            generate_table(
                manage_coffee_items_list(), 
                ['Choice', 'Item'], 
                'bright_blue', 
                'Manage Coffee Items'
                )
            coffee_items_choice = int(input())
            manage_coffee_items(coffee_items_choice)
            print('')

        case 'c':
            return
        
def handle_selection(choice):
    choice_list = str.split(COFFEE_SELECTION_LIST[choice - 1])
    if len(choice_list) >= 3:
        coffe_choice = " ".join([choice_list[1], choice_list[2]]).lower()
    else:
        coffe_choice = choice_list[1].lower()
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
