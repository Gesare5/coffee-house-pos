import pytest

import coffee_model


class TestCoffee:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.coffee = coffee_model.Coffee(["caffe latte", 150, 16, 30, 0, 0, 12])

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.coffee

    def test_get_quantities_consumed(self):
        assert self.coffee.get_quantities_consumed() == {
            "milk": 150,
            "coffee": 16,
            "sugar": 30,
            "vanilla": 0,
            "cocoa": 0,
        }

    def test_subtract_quantitites_from_total(self):
        result = self.coffee.subtract_quantitites_from_total(
            {
                "coffee": 200,
                "milk": 200,
                "sugar": 200,
                "vanilla": 200,
                "cocoa": 200,
            }
        )
        assert result == {
            "milk": 50,
            "coffee": 184,
            "sugar": 170,
            "vanilla": 200,
            "cocoa": 200,
        }
