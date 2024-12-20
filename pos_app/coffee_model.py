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
        totals["milk"] = float(totals["milk"]) - self.milk
        totals["sugar"] = float(totals["sugar"]) - self.sugar
        totals["coffee"] = float(totals["coffee"]) - self.coffee

        if self.type == "vanilla latte":
            totals["vanilla"] = float(totals["vanilla"]) - self.vanilla
        if self.type == "caffe mocha":
            totals["cocoa"] = float(totals["cocoa"]) - self.cocoa
        return totals
