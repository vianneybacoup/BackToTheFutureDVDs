from .Saga import Saga

from .constants import DEFAULT_DVD_PRICE, END_OF_INPUT_SHOPPING_LIST


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

    (price_saga, count_saga) = Saga.get_all_price_and_count(shopping_list, saga_list)

    count_not_saga = len(shopping_list) - count_saga
    price_not_saga = count_not_saga * DEFAULT_DVD_PRICE

    return price_saga + price_not_saga


def shopping_list_from_input():
    shopping_list = []
    while True:
        dvd_title = input()
        if dvd_title == END_OF_INPUT_SHOPPING_LIST:
            break
        shopping_list = shopping_list + [dvd_title]

    return shopping_list
