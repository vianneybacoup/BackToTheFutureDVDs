from .Saga import Saga

from .constants import DEFAULT_DVD_PRICE, EOF_SHOPPING_CART_LIST


saga_list = [
    Saga([
        "Back to the Future 1",
        "Back to the Future 2",
        "Back to the Future 3"
    ], [
        15,
        15 * 0.9,
        15 * 0.8
    ])
]


def shopping_cart_price_calculation():
    shopping_list = shopping_list_from_input()

    (saga_total_price, saga_total_count) = get_all_saga_price_and_count(shopping_list)

    shopping_list_count_not_a_saga = len(shopping_list) - saga_total_count
    sum_of_not_saga_price = shopping_list_count_not_a_saga * DEFAULT_DVD_PRICE

    return saga_total_price + sum_of_not_saga_price


def shopping_list_from_input():
    shopping_list = []
    while True:
        dvd_title = input()
        if dvd_title == EOF_SHOPPING_CART_LIST:
            break
        shopping_list = shopping_list + [dvd_title]

    return shopping_list


def get_all_saga_price_and_count(shopping_list):
    saga_total_price = 0
    saga_total_count = 0

    for saga in saga_list:
        (current_saga_total_price, current_saga_total_count) = saga.get_price_and_count(shopping_list)
        saga_total_price = saga_total_price + current_saga_total_price
        saga_total_count = saga_total_count + current_saga_total_count

    return (saga_total_price, saga_total_count)
