from abc import ABC, abstractmethod


class PromotionStrategy(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def do_promotion(self):
        pass


class NewYearPromotion(PromotionStrategy):
    def __init__(self, price):
        super().__init__(price)

    def do_promotion(self):
        return self.price * 0.5


class BlackFridayPromotion(PromotionStrategy):
    def __init__(self, price):
        super().__init__(price)

    def do_promotion(self):
        return self.price * 0.1


class FifthOfMayPromotion(PromotionStrategy):
    def __init__(self, price):
        super().__init__(price)

    def do_promotion(self):
        return self.price * 0.8


class PromotionContext:
    def __init__(self, strategy):
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy = strategy

    def get_price(self):
        return self.__strategy.do_promotion()


def main():
    promotion_new_year = NewYearPromotion(100)
    promotion_context = PromotionContext(promotion_new_year)
    print(promotion_context.get_price())

    promotion_context.strategy = BlackFridayPromotion(100)
    print(promotion_context.get_price())

    promotion_context.strategy = FifthOfMayPromotion(100)
    print(promotion_context.get_price())


if __name__ == '__main__':
    main()
