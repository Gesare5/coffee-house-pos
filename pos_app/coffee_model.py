class Coffee:
    def __init__(self, milk, sugar, coffee, type, id):
        self.milk = milk       # in ml
        self.coffee = coffee   # in grams
        self.sugar = sugar     # in grams
        self.type = type
        self.id = id

    def get_quantities_consumed(self):
        return {
            'milk': self.milk,
            'sugar': self.sugar,
            'coffee': self.coffee
        }



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