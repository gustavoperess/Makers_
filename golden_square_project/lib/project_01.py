import random
from twilio.rest import Client
from datetime import datetime, timedelta
from keys import My_Keys


class Order:
    def __init__(self, name: str, phone_number):
        self.dict_of_items = {}
        self.menu = The_Burger_Place()
        self.name = name
        self.order_number = random.randint(1045678, 1234567)
        self.my_keys = My_Keys()
        self.account_sid = self.my_keys.login
        self.auth_token = self.my_keys.key
        self.phone_number = phone_number
        self.final_price = 0
        now = datetime.now()
        time_plus_thirty_minutes = now + timedelta(minutes=30)
        self.time_plus_thirty_minutes_formatted = time_plus_thirty_minutes.strftime("%H:%M:%S")

    def show_menu(self):
        return self.menu.list_of_items()

    def add_item(self, order_entry):
        for item, price in self.menu.list_of_items().items():
            if item == order_entry.order and order_entry.order_is_on:
                self.dict_of_items[item] = price

    def _format_items(self):
        return " and ".join([f"{item}: ${price}" for item, price in self.dict_of_items.items()])

    def show_items_added(self):
        result = self._format_items()
        return f"{self.name}, please see what you've ordered so far: a {result}"

    def receipt(self):
        if not self.dict_of_items:
            return f"No items in the order for {self.name}."

        self.final_price = sum(self.dict_of_items.values())
        result = self._format_items()
        return f"{self.name}, order number #{self.order_number} a {result} final price {self.final_price}"

    def order_confirmation_by_text(self):
        client = Client(self.account_sid, self.auth_token)
        self.final_price = sum(self.dict_of_items.values())
        message = client.messages.create(
            from_='+15057507904',
            body=f"{self.name} Thank you! Your order #{self.order_number} of {self._format_items()} "
                 f"coming to a total of {self.final_price} has been placed and will be delivered before {self.time_plus_thirty_minutes_formatted}",
            to=f'+{self.phone_number}'
        )
        return message


class Order_entry:
    def __init__(self, customer_order):
        self.order = customer_order
        self.order_is_on = True

    def is_order_still_on(self):
        self.order_is_on = False


class The_Burger_Place:
    def __init__(self):
        self.burger_menu = {}

    def list_of_items(self):
        self.burger_menu = {
            "Classic Cheeseburger": 8.99,
            "Bacon BBQ Burger": 9.99,
            "Mushroom Swiss Burger": 10.49,
            "Veggie Burger": 7.99,
            "Spicy Jalapeño Burger": 9.49,
            "Turkey Avocado Burger": 10.99,
            "Blue Cheese Bacon Burger": 11.49,
            "Hawaiian Teriyaki Burger": 12.99,
            "Southwestern Chipotle Burger": 10.99,
            "Salmon Burger": 13.99,
        }

        return self.burger_menu


order = Order("Gustavo", 17783179738)
entry_01 = Order_entry("Classic Cheeseburger")
entry_02 = Order_entry("Hawaiian Teriyaki Burger")

order.add_item(entry_01)
order.add_item(entry_02)
# print(order.order_confirmation_by_text())
