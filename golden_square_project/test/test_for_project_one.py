from lib.project_01 import *
from unittest.mock import Mock, patch


def test_if_a_dictionary_of_items_is_show():
    my_oder = Order("Gustavo", 7783179738)
    the_burger_place = Mock()
    the_burger_place.list_of_items()
    result = my_oder.show_menu()
    assert result == {"Classic Cheeseburger": 8.99,
                      "Bacon BBQ Burger": 9.99,
                      "Mushroom Swiss Burger": 10.49,
                      "Veggie Burger": 7.99,
                      "Spicy Jalapeño Burger": 9.49,
                      "Turkey Avocado Burger": 10.99,
                      "Blue Cheese Bacon Burger": 11.49,
                      "Hawaiian Teriyaki Burger": 12.99,
                      "Southwestern Chipotle Burger": 10.99,
                      "Salmon Burger": 13.99, }


def test_shows_nothing_has_been_added():
    the_burger_place = Mock()
    the_burger_place.list_of_items().result_value = {"Classic Cheeseburger": 8.99}
    my_order = Order("Gustavo", 778317938)
    first_entry = Mock("")
    first_entry.order = ""
    first_entry.order_is_on = True
    my_order.add_item(first_entry)
    result = my_order.receipt()
    assert result == "No items in the order for Gustavo."


def test_to_show_what_has_been_added_so_far():
    the_burger_place = Mock()
    the_burger_place.list_of_items().result_value = {"Classic Cheeseburger": 8.99, "Hawaiian Teriyaki Burger": 12.99}
    my_order = Order("Gustavo", 7783179728)
    first_entry = Mock("Classic Cheeseburger")
    second_entry = Mock("Hawaiian Teriyaki Burger")
    first_entry.order = "Classic Cheeseburger"
    second_entry.order = "Hawaiian Teriyaki Burger"
    first_entry.order_is_on = True
    second_entry.order_is_on = True
    my_order.add_item(first_entry)
    my_order.add_item(second_entry)
    result = my_order.show_items_added()
    assert result == "Gustavo, please see what you've ordered so far: a Classic Cheeseburger: $8.99 and Hawaiian Teriyaki Burger: $12.99"


def test_to_show_my_receipt():
    with patch.object(random, 'randint', return_value=1208787):
        the_burger_place = Mock()
        the_burger_place.list_of_items().result_value = {"Classic Cheeseburger": 8.99,
                                                         "Hawaiian Teriyaki Burger": 12.99}
        my_order = Order("Gustavo", 7783179738)
        first_entry = Mock("Classic Cheeseburger")
        second_entry = Mock("Hawaiian Teriyaki Burger")
        first_entry.order = "Classic Cheeseburger"
        second_entry.order = "Hawaiian Teriyaki Burger"
        first_entry.order_is_on = True
        second_entry.order_is_on = True
        my_order.add_item(first_entry)
        my_order.add_item(second_entry)
        result = my_order.receipt()
        assert result == (f"Gustavo, order number #1208787 a Classic Cheeseburger: $8.99 and Hawaiian "
                          f"Teriyaki Burger: "
                          "$12.99 final price 21.98")


def test_order_confirmation_by_text():
    with patch.object(random, 'randint', return_value=1208787):
        instance = Order(name='Gustavo', phone_number='+17783179738')
        mock_client = Mock()
        first_entry = Mock()
        second_entry = Mock()
        first_entry.order = "Classic Cheeseburger"
        second_entry.order = "Hawaiian Teriyaki Burger"
        first_entry.order_is_on = True
        second_entry.order_is_on = True

        instance.add_item(first_entry)
        instance.add_item(second_entry)

        mock_messages_create = Mock()
        mock_client.return_value.messages.create = mock_messages_create

        result = instance.order_confirmation_by_text()

        mock_client.assert_called_once_with(instance.account_sid, instance.auth_token)
        mock_messages_create.assert_called_once_with(
            from_='+15057507904',
            body=f"Gustavo, Thank you! Your order #1208787 a Classic Cheeseburger: $8.99 and Hawaiian Teriyaki Burger: "
                 f"$12.99 final price 21.98 has been placed and will be delivered before 12:30:20",
            to='+7783179738'
        )

        expected_result = (
            f"Gustavo, Thank you! Your order #1208787 a Classic Cheeseburger: $8.99 and Hawaiian Teriyaki Burger: $12.99 "
            f"final price 21.98 has been placed and will be delivered before 12:30:20")
        assert result == expected_result
