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

        saga = intersection(shopping_list, self.titles)
        count_saga = len(saga)

        distinct_saga = list(set(saga))
        count_distinct_saga = len(distinct_saga)

        price_one_saga = self.get_price_from_distinct(count_distinct_saga)
        return (
            price_one_saga * count_saga,
            count_saga
        )


    def get_price_from_distinct(self, distinct_count):
        try:
            return self.price_rules[distinct_count - 1]
        except KeyError:
            return DEFAULT_DVD_PRICE   


    @staticmethod
    def get_all_price_and_count(shopping_list, saga_list):
        price_saga = 0
        count_saga = 0

        for saga in saga_list:
            (price_current_saga, count_current_saga) = saga.get_price_and_count(shopping_list)
            price_saga = price_saga + price_current_saga
            count_saga = count_saga + count_current_saga

        return (price_saga, count_saga)
