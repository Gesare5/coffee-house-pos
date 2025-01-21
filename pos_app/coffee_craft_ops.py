from datetime import date, datetime
from coffee_model import Coffee
from data_store_operations import DataStoreOperations
from utils import generate_table, generate_alert


def get_totals():
    try:
        read_list = DataStoreOperations.read_from_store("inventory.csv")
        totals = {}
        for value in read_list:
            if value and value[0] is not None:
                totals[value[0]] = float(value[1])

        return totals
    except:
        print("Failed to fetch inventory totals from store!!")


def get_thresholds():
    try:
        read_list = DataStoreOperations.read_from_store("thresholds.csv")
        thresholds = {}
        for value in read_list:
            thresholds[value[0]] = float(value[1])

        return thresholds
    except:
        print("Failed to fetch inventory thresholds from store!!")


def populate_coffee_items():
    data = [
        ["coffee_type", "milk", "coffee", "sugar", "vanilla", "cocoa", "cost"],
        ["caffe latte", 150, 18, 30, 0, 0, 12],
        ["vanilla latte", 150, 18, 30, 30, 0, 14],
        ["espresso", 0, 18, 30, 0, 0, 10],
        ["cappuccino", 150, 18, 30, 0, 0, 14.5],
        ["caffe mocha", 120, 16, 35, 0, 30, 13],
    ]
    try:
        DataStoreOperations.write_to_store("coffee_items.csv", data)
    except:
        print("Failed to populate coffee items store!!")


def generate_coffee_list() -> list[str]:
    try:
        read_list = DataStoreOperations.read_from_store("coffee_items.csv")
        coffee_list = []
        for i, value in enumerate(read_list):
            if i > 0:
                coffee_item = "{0}: {1}".format(i, value[0])
                coffee_list.append(coffee_item)
        return coffee_list
    except:
        print("Failed to generate coffee list!!")


def generate_coffee_table_list() -> list[str]:
    try:
        read_list = DataStoreOperations.read_from_store("coffee_items.csv")
        coffee_list = []
        for i, value in enumerate(read_list):
            if i > 0:
                coffee_item = [str(i), value[0], value[len(value) - 1]]
                coffee_list.append(coffee_item)
        return coffee_list
    except:
        print("Failed to generate coffee table list!!")


def create_coffee_items_object():
    try:
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
    except:
        print("Failed to create coffee items object!!")


def manage_coffee_items(choice):
    if choice == 1:
        add_coffee_item()
    elif choice == 2:
        remove_coffee_item(generate_coffee_list())
    elif choice == 4:
        supplies = ["1: Milk", "2: Coffee", "3: Sugar", "4: Cocoa", "5: Vanilla"]
        # Read this from file
        print("Select supply: ")
        for supply in supplies:
            print(supply)
        supply = int(input())
        print("")
        print("Amount in grams/millilitre: ")
        amount = input()
        print("")
        replenish_inventory(supplies[supply - 1], amount)

    else:
        generate_table(
            generate_coffee_table_list(),
            ["Choice", "Coffee", "Cost"],
            ["bright_blue", "bright_magenta", "bright_green"],
            "Coffee List",
        )


def craft_a_coffee(coffee_type):
    try:
        # create a coffee object
        read_list = DataStoreOperations.read_from_store("coffee_items.csv")
        for coffee_item in read_list:
            if coffee_type == coffee_item[0]:
                coffee = Coffee(coffee_item)
                print("Successfully created coffee!")

        # subtract quantities
        new_totals = coffee.subtract_quantitites_from_total(get_totals())

        # Save new totals to file
        store_data = [
            ["coffee", new_totals["coffee"]],
            ["milk", new_totals["milk"]],
            ["sugar", new_totals["sugar"]],
            ["vanilla", new_totals["vanilla"]],
            ["cocoa", new_totals["cocoa"]],
        ]
        DataStoreOperations.write_to_store("inventory.csv", store_data)

        # Save to daily report
        report_name = "Daily_Sales_{0}.csv".format(date.today())
        report_data = [coffee.type, coffee.cost, datetime.time(coffee.created_at)]
        DataStoreOperations.write_to_store(report_name, [report_data])
    except:
        print("Failed to update inventory and generate report!!")
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
    try:
        DataStoreOperations.write_to_store("coffee_items.csv", [new_coffee_item])
    except:
        print("Failed to add coffee item!!")


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

    try:
        # read store and remove selected coffee_item from list
        coffee_items_list = DataStoreOperations.read_from_store("coffee_items.csv")
        for i, value in enumerate(coffee_items_list):
            if coffee_items_list[i][0] == coffee_choice:
                coffee_items_list.remove(value)

        # Publish altered list (with removed coffee_item) to store
        DataStoreOperations.overwrite_store("coffee_items.csv", coffee_items_list)
    except:
        print("Failed to update remove coffee item!!")


def calculate_total_daily_sales(day):
    report_name = "Daily_Sales_{0}.csv".format(day)
    total_sale = 0
    try:
        read_list = DataStoreOperations.read_from_store(report_name)
        for _, coffee_item in enumerate(read_list):
            total_sale = total_sale + float(coffee_item[1])
        return total_sale
    except:
        print("Failed to fetch sales for {0}!!".format(day))


def print_daily_report(day):
    report_name = "Daily_Sales_{0}.csv".format(day)
    try:
        read_list = DataStoreOperations.read_from_store(report_name)
        generate_table(
            read_list,
            ["Coffee", "Cost", "Created At"],
            ["bright_blue", "bright_green", "bright_magenta"],
            "Daily_Report_{0}".format(day),
        )
    except:
        print("Failed to fetch report!!")


def print_receipt(coffees_per_customer):
    receipt_list = []
    total = 0
    for coffee in coffees_per_customer:
        subtotal = float(coffee[1]) * float(coffee[2])
        coffee_item = [
            coffee[0],
            coffee[1],
            "x {0}".format(coffee[2]),
            str(subtotal),
        ]
        receipt_list.append(coffee_item)
        total = total + subtotal

    receipt_list.append(["", "", "", ""])
    receipt_list.append(["total", "", "", str(total)])
    print("")
    generate_table(
        receipt_list,
        ["Coffee", "Cost", "Quantity", "Subtotal"],
        [
            "bright_blue",
            "bright_green",
            "bright_magenta",
            "bright_green",
        ],
        "RECEIPT",
    )
    print("")


def check_remaining_quantities():
    thresholds = get_thresholds()
    totals = get_totals()
    if totals["milk"] < thresholds["milk"]:
        generate_alert("milk", totals["milk"], "ml")

    if totals["sugar"] < thresholds["sugar"]:
        generate_alert("sugar", totals["sugar"], "g")

    if totals["coffee"] < thresholds["coffee"]:
        generate_alert("coffee", totals["coffee"], "g")

    if totals["vanilla"] < thresholds["vanilla"]:
        generate_alert("vanilla", totals["vanilla"], "ml")

    if totals["cocoa"] < thresholds["cocoa"]:
        generate_alert("cocoa", totals["cocoa"], "g")

    return


def replenish_inventory(supply_item, amount):
    supply = str.lower(str.split(supply_item)[1])
    totals = get_totals()
    totals[supply] = float(totals[supply]) + float(amount)
    store_data = [
        ["coffee", totals["coffee"]],
        ["milk", totals["milk"]],
        ["sugar", totals["sugar"]],
        ["vanilla", totals["vanilla"]],
        ["cocoa", totals["cocoa"]],
    ]
    try:
        DataStoreOperations.write_to_store("inventory.csv", store_data)
        print("Successfully updated inventory!!")
    except:
        print("Failed to update inventory!!")


# TODO ADD CHECK FOR NON EXISTENT FILES / OR EMPTY FILES AND MANAGE ERRORS
# add docstrings to functions
