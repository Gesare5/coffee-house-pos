class Coffee:
    def __init__(self, coffee_item):
        self.type = coffee_item[0]
        self.milk = float(coffee_item[1])  # in ml
        self.coffee = float(coffee_item[2])  # in grams
        self.sugar = float(coffee_item[3])  # in grams
        self.vanilla = float(coffee_item[4])  # in grams
        self.cocoa = float(coffee_item[5])  # in ml
        self.cost = float(coffee_item[6])

    def get_quantities_consumed(self):
        return {"milk": self.milk, "sugar": self.sugar, "coffee": self.coffee}

    def subtract_quantitites_from_total(self, totals):
        totals["milk"] = totals["milk"] - self.milk
        totals["sugar"] = totals["sugar"] - self.sugar
        totals["coffee"] = totals["coffee"] - self.coffee

        if self.type == "vanilla latte":
            totals["vanilla"] = totals["vanilla"] - self.vanilla
        if self.type == "caffe mocha":
            totals["cocoa"] = totals["cocoa"] - self.cocoa
        return totals

    def check_remaining_quantities(self, totals, thresholds):
        if totals["milk"] < thresholds["milk"]:
            print("Alert!! Running out of milk")
            print("Amount of milk left: ", totals["milk"], "ml")
            print("")

        if totals["sugar"] < thresholds["sugar"]:
            print("Alert!! Running out of sugar")
            print("Amount of sugar left: ", totals["sugar"], "g")
            print("")

        if totals["coffee"] < thresholds["coffee"]:
            print("Alert!! Running out of coffee")
            print("Amount of coffee left: ", totals["coffee"], "g")
            print("")

        if totals["vanilla"] < thresholds["vanilla"]:
            print("Alert!! Running out of vanilla")
            print("Amount of vanilla left: ", totals["vanilla"], "ml")
            print("")

        if totals["cocoa"] < thresholds["cocoa"]:
            print("Alert!! Running out of cocoa")
            print("Amount of cocoa left: ", totals["cocoa"], "g")
            print("")

        return
