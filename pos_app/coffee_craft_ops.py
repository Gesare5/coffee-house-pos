from coffee_model import Coffee
from data_store_operations import DataStoreOperations
from utils import generate_table


def get_totals():
    return {
        "coffee": 10000,  # g
        "milk": 10000,  # ml
        "sugar": 10000,  # g
        "cocoa": 200,  # g
    }


def get_thresholds():
    return {
        "coffee": 10000,  # g
        "milk": 10000,  # ml
        "sugar": 10000,  # g
        "cocoa": 200,  # g
    }


def populate_coffee_items():
    data = [
        ["coffee_type", "milk", "coffee", "sugar", "vanilla", "cocoa", "cost"],
        ["caffe latte", 150, 18, 30, 0, 0, 12],
        ["vanilla latte", 150, 18, 30, 30, 0, 14],
        ["espresso", 0, 18, 30, 0, 0, 10],
        ["cappuccino", 150, 18, 30, 0, 0, 14.5],
        ["caffe mocha", 120, 16, 35, 0, 30, 13],
    ]
    DataStoreOperations.write_to_store("coffee_items.csv", data)


def generate_coffee_list() -> list[str]:
    read_list = DataStoreOperations.read_from_store("coffee_items.csv")
    coffee_list = []
    for i, value in enumerate(read_list):
        if i > 0:
            coffee_item = "{0}: {1}".format(i, value[0])
            coffee_list.append(coffee_item)
    return coffee_list


def generate_coffee_table_list() -> list[str]:
    read_list = DataStoreOperations.read_from_store("coffee_items.csv")
    coffee_list = []
    for i, value in enumerate(read_list):
        if i > 0:
            coffee_item = [str(i), value[0], value[len(value) - 1]]
            coffee_list.append(coffee_item)
    return coffee_list


def create_coffee_items_object():
    coffee_items_list = DataStoreOperations.read_from_store("coffee_items.csv")
    coffee_items_dict = {}

    for i, _ in enumerate(coffee_items_list):
        if i < len(coffee_items_list) - 1:
            sub_dict = {}
            inner_list = coffee_items_list[i + 1]
            for j, _ in enumerate(inner_list, 1):
                if j < len(inner_list) - 1:
                    sub_dict[coffee_items_list[0][j]] = float(inner_list[j + 1])
            coffee_items_dict[inner_list[0]] = sub_dict

    return coffee_items_dict


def manage_coffee_items(choice):
    if choice == 1:
        add_coffee_item()
    elif choice == 2:
        remove_coffee_item(generate_coffee_list())
    else:
        generate_table(
            generate_coffee_table_list(),
            ["Choice", "Coffee", "Cost"],
            ["bright_blue", "bright_magenta", "bright_green"],
            "Coffee List",
        )


def craft_a_coffee(coffee_type):
    coffee_items = create_coffee_items_object()
    coffee_details = coffee_items[coffee_type]

    # create a coffee object
    coffee = Coffee(
        coffee_type,
        coffee_details["milk"],
        coffee_details["coffee"],
        coffee_details["sugar"],
    )

    # subtract quantities
    new_totals = coffee.subtract_quantitites_from_total(get_totals())

    # check quantities left, if below threshold create an alert!
    coffee.check_remaining_quantities(new_totals, get_thresholds())
    return


def add_coffee_item():
    print("Coffee_type? ")
    coffee_type = input()
    print("Milk Amount: ")
    milk = input()
    print("Coffee Amount: ")
    coffee = input()
    print("Sugar Amount: ")
    sugar = input()
    print("Vanilla: ")
    vanilla = input()
    print("Cocoa: ")
    cocoa = input()
    print("Cost: ")
    cost = input()

    new_coffee_item = [coffee_type, milk, coffee, sugar, vanilla, cocoa, cost]
    DataStoreOperations.write_to_store("coffee_items.csv", [new_coffee_item])


def remove_coffee_item(coffee_list):
    # Print coffee menu selection
    for value in coffee_list:
        print(value)
    choice = int(input())
    choice_list = str.split(coffee_list[choice - 1])
    if len(choice_list) >= 3:
        coffee_choice = " ".join([choice_list[1], choice_list[2]]).lower()
    else:
        coffee_choice = choice_list[1].lower()

    # read store and remove selected coffee_item from list
    coffee_items_list = DataStoreOperations.read_from_store("coffee_items.csv")
    for i, value in enumerate(coffee_items_list):
        if coffee_items_list[i][0] == coffee_choice:
            coffee_items_list.remove(value)

    # Publish altered list (with removed coffee_item) to store
    DataStoreOperations.overwrite_store("coffee_items.csv", coffee_items_list)
