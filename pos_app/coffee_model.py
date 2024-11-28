class Coffee:
    def __init__(self, coffe_type, milk, coffee, sugar):
        self.milk = milk  # in ml
        self.coffee = coffee  # in grams
        self.sugar = sugar  # in grams
        self.type = coffe_type

    def get_quantities_consumed(self):
        return {"milk": self.milk, "sugar": self.sugar, "coffee": self.coffee}

    def subtract_quantitites_from_total(self, totals):
        totals["milk"] = totals["milk"] - self.milk
        totals["sugar"] = totals["sugar"] - self.sugar
        totals["coffee"] = totals["coffee"] - self.coffee

        # if self.type == 'vanilla latte':
        # totals['vanilla'] = totals['vanilla'] - self.extras.vanilla
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
            print("Alert!! Running out of coffe")
            print("Amount of coffee left: ", totals["coffee"], "g")
            print("")
        return


# TODO
# HANDLE ALL THIS REPETITION
# ALLOW SELECTION OF MULTIPLE COFFEES AND COFFE MULTIPLES

# caffe latte ->
# 150ml steamed milk
# 18g ground coffee beans
# sugar - how  many

# vanilla latte ->
# 150ml steamed milk
# 18g ground coffee beans
# 2 tbsp/ 30 ml vanilla syrup
# sugar - how  many

# espresso ->
# 18 g coffee beans
# 1.5 * 18g water

# Cappuccino ->
# 18 g coffee beans
# 60 ml steamed milk
# 60 ml foamed milk

# caffe mocha ->
# 2 tbsp/ 28.3g cocoa powder
# 2.84g / 1/2 teaspoon sugar
# 16 g coffee beans
# 15 ml hot water
# 120 ml steamed milk
