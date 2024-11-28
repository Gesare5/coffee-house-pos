from coffee_model import Coffee


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


# Todo: keep track of units...


def coffee_items():
    return {
        "cafe latte": {"milk": 150, "coffee": 18, "sugar": 30},
        "vanilla latte": {"milk": 150, "coffee": 18, "sugar": 30, "vanilla syrup": 30},
        "espresso": {"coffee": 18, "sugar": 30},
        "cappuccino": {"milk": 150, "coffee": 18, "sugar": 30},
        "caffe mocha": {"milk": 120, "coffee": 16, "sugar": 35, "cocoa": 30},
    }


def craft_a_coffee(coffee_type):
    coffee_details = coffee_items()[coffee_type]
    # create a coffee object
    coffee = Coffee(  # starting with basic latte
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
