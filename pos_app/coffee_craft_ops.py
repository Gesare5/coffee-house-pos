from coffee_model import Coffee
from data_store_operations import read_from_store, write_to_store


def get_totals():
    return {
        "coffee": 10000,  # g
        "milk": 10000,  # ml
        "sugar": 10000,  # g
        "cocoa": 200,  # g
    }


# TODO: keep track of units...


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
    write_to_store("coffee_items.csv", data)


def create_coffee_items_object():
    coffee_items_list = read_from_store("coffee_items.csv")
    coffee_items_dict = {}
    # make enumerate start from index = 1
    for i, v in enumerate(coffee_items_list):
        if i < len(coffee_items_list) - 1:
            sub_dict = {}
            inner_list = coffee_items_list[i + 1]
            for j, v in enumerate(inner_list):
                if j < len(inner_list) - 1:
                    sub_dict[coffee_items_list[0][j + 1]] = float(inner_list[j + 1])
            coffee_items_dict[inner_list[0]] = sub_dict

    return coffee_items_dict


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
