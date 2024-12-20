from datetime import date
from coffee_craft_ops import (
    generate_coffee_list,
    generate_coffee_table_list,
    craft_a_coffee,
    manage_coffee_items,
    print_receipt,
    check_remaining_quantities
)
from utils import generate_table


COFFEE_SELECTION_LIST = generate_coffee_list()
COFFEE_TABLE_SELECTION_LIST = generate_coffee_table_list()


def prelim_list() -> list[str]:
    print("")
    return [
        "A: Order Coffee",
        "B: Manage Coffee Items",
        "C: Exit",
    ]


def manage_coffee_items_list():
    print("")
    return [
        ["1", "Add Coffee Item"],
        ["2", "Delete Coffee Item"],
        ["3", "View Coffee Items"],
    ]


def handle_prelim_action(action):
    match action:
        case "a":
            COFFEE_TABLE_SELECTION_LIST.append(["0", "Done!!", ""])
            coffees_per_customer = []
            while True:
                print("")
                generate_table(
                    COFFEE_TABLE_SELECTION_LIST,
                    ["Choice", "Coffee", "Cost"],
                    ["bright_blue", "bright_magenta", "bright_green"],
                    "Coffee List",
                )
                coffee_choice = input()
                if coffee_choice.isdigit() and int(coffee_choice) < len(
                    COFFEE_TABLE_SELECTION_LIST
                ):
                    if coffee_choice == "0":
                        break
                    else:
                        print("How many? ")
                        quantity = input()
                        if quantity.isdigit():
                            handle_selection(int(coffee_choice), int(quantity))
                            coffees = [
                                COFFEE_TABLE_SELECTION_LIST[int(coffee_choice) - 1][1],
                                COFFEE_TABLE_SELECTION_LIST[int(coffee_choice) - 1][2],
                                int(quantity),
                            ]
                            coffees_per_customer.append(coffees)
                            print("")
                            print("Anything Else? ")
                            print("")
                        else:
                            print("Invalid value!!")
                            print("")
                            break
                else:
                    print("Invalid Choice!!")
                    continue
                
            print_receipt(coffees_per_customer)
            # check quantities left, if below threshold create an alert!
            check_remaining_quantities()

        case "b":
            print("")
            generate_table(
                manage_coffee_items_list(),
                ["Choice", "Item"],
                ["bright_blue"],
                "Manage Coffee Items",
            )
            coffee_items_choice = int(input())
            manage_coffee_items(coffee_items_choice)
            print("")

        case "c":
            return


def handle_selection(choice, quantity):
    choice_list = str.split(COFFEE_SELECTION_LIST[choice - 1])
    if len(choice_list) >= 3:
        coffee_type = " ".join([choice_list[1], choice_list[2]]).lower()
    else:
        coffee_type = choice_list[1].lower()
    for i in range(quantity):
        craft_a_coffee(coffee_type)
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
        if prelim_action == "c":
            break
        else:
            handle_prelim_action(prelim_action)


if __name__ == "__main__":
    main()
