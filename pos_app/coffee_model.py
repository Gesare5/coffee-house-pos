from datetime import datetime
from utils import generate_table


class Coffee:
    def __init__(self, coffee_item):
        self.type = coffee_item[0]
        self.milk = float(coffee_item[1])  # in ml
        self.coffee = float(coffee_item[2])  # in grams
        self.sugar = float(coffee_item[3])  # in grams
        self.vanilla = float(coffee_item[4])  # in grams
        self.cocoa = float(coffee_item[5])  # in ml
        self.cost = float(coffee_item[6])
        self.created_at = datetime.now()

    def get_quantities_consumed(self):
        return {
            "milk": self.milk,
            "sugar": self.sugar,
            "coffee": self.coffee,
            "vanilla": self.vanilla,
            "cocoa": self.cocoa,
        }

    def subtract_quantitites_from_total(self, totals):
        totals["milk"] = totals["milk"] - self.milk
        totals["sugar"] = totals["sugar"] - self.sugar
        totals["coffee"] = totals["coffee"] - self.coffee

        if self.type == "vanilla latte":
            totals["vanilla"] = totals["vanilla"] - self.vanilla
        if self.type == "caffe mocha":
            totals["cocoa"] = totals["cocoa"] - self.cocoa
        return totals

    def generate_alert(self, title, total_value, unit):
        alert = [
            "Alert!! Running out of {0}.\nAmount of {0} left: {1} {2}.".format(
                title, total_value, unit
            )
        ]
        generate_table(
            [alert],
            ["Alert!"],
            ["bright_red"],
            "",
        )
        print("")

    def check_remaining_quantities(self, totals, thresholds):
        if totals["milk"] < thresholds["milk"]:
            self.generate_alert("milk", totals["milk"], "ml")

        if totals["sugar"] < thresholds["sugar"]:
            self.generate_alert("sugar", totals["sugar"], "g")

        if totals["coffee"] < thresholds["coffee"]:
            self.generate_alert("coffee", totals["coffee"], "g")

        if totals["vanilla"] < thresholds["vanilla"]:
            self.generate_alert("vanilla", totals["vanilla"], "ml")

        if totals["cocoa"] < thresholds["cocoa"]:
            self.generate_alert("cocoa", totals["cocoa"], "g")

        return
