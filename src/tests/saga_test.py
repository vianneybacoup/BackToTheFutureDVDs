from src.Saga import Saga
from src.shopping_cart import shopping_cart_price_calculation
from src.constants import DEFAULT_DVD_PRICE

from unittest import TestCase

def create_fake_saga():
    return [Saga(
        ["Back to the Future 1", "Back to the Future 2", "Back to the Future 3"],
        [15, 15 * 0.9, 15 * 0.8]
    )]


class SagaTest(TestCase):
    def test_when_empty_shopping_list_price_should_be_zero(self):
        sagas = create_fake_saga()
        shopping_list = []

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = 0
        self.assertEqual(calculated_price, expected_price)


    def test_when_buying_one_movie_not_in_a_saga_price_should_be_default_price(self):
        sagas = create_fake_saga()
        shopping_list = ["Not in a saga"]

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = DEFAULT_DVD_PRICE
        self.assertEqual(calculated_price, expected_price)


    def test_when_buying_one_saga_movie_price_should_be_saga_price(self):
        sagas = create_fake_saga()
        shopping_list = ["Back to the Future 1"]

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = sagas[0].price_rules[0]
        self.assertEqual(calculated_price, expected_price)


    def test_when_buying_twice_a_saga_movie_price_should_be_saga_price_times_two(self):
        sagas = create_fake_saga()
        shopping_list = ["Back to the Future 1", "Back to the Future 1"]

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = sagas[0].price_rules[0] * len(shopping_list)
        self.assertEqual(calculated_price, expected_price)


    def test_when_buying_two_distinct_saga_movie_price_should_be_with_reduction(self):
        sagas = create_fake_saga()
        shopping_list = ["Back to the Future 1", "Back to the Future 2"]

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = sagas[0].price_rules[1] * len(shopping_list)
        self.assertEqual(calculated_price, expected_price)


    def test_when_buying_all_saga_movies_and_a_not_saga_movie(self):
        sagas = create_fake_saga()
        shopping_list = ["Back to the Future 1", "Back to the Future 2", "Back to the Future 3", "Not in a saga"]

        calculated_price = shopping_cart_price_calculation(shopping_list, sagas)

        expected_price = sagas[0].price_rules[2] * 3 + DEFAULT_DVD_PRICE
        self.assertEqual(calculated_price, expected_price)
