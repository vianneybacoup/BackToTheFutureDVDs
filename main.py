from src.shopping_cart import shopping_list_from_input, shopping_cart_price_calculation
from src.Saga import Saga


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


if __name__ == '__main__':
    print("""
          Enter your movie shopping list (one row per movie).
          Enter an empty row when you listed everything.
    """)
    shopping_list = shopping_list_from_input()

    print("Price of your shopping cart:", shopping_cart_price_calculation(shopping_list, saga_list))
