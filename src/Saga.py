from .utils import intersection
from .constants import DEFAULT_DVD_PRICE

class Saga:
    def __init__(self, titles, price_rules):
        self.titles = titles
        self.price_rules = price_rules

    def get_price_and_count(self, shopping_list):
        if (len(self.titles) == 0):
            return (0, 0)

        if (len(shopping_list) == 0):
            return (0, 0)

        dvd_of_saga_in_shopping_list = intersection(shopping_list, self.titles)
        number_dvd_of_saga_in_shopping_list = len(dvd_of_saga_in_shopping_list)

        distinct_dvd_of_saga_in_shopping_list = list(set(dvd_of_saga_in_shopping_list))
        number_distinct_dvd_of_saga_in_shopping_list = len(distinct_dvd_of_saga_in_shopping_list)

        one_dvd_price = self.get_price_from_distinct(number_distinct_dvd_of_saga_in_shopping_list)
        return (
            one_dvd_price * number_dvd_of_saga_in_shopping_list,
            number_dvd_of_saga_in_shopping_list
        )

    def get_price_from_distinct(self, distinct_count):
        try:
            return self.price_rules[distinct_count - 1]
        except KeyError:
            return DEFAULT_DVD_PRICE
