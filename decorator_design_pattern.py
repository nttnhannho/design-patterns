from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def do_pizza(self):
        pass


class TomatoPizza(Pizza):
    def do_pizza(self):
        return "I am Tomato pizza"


class ChickenPizza(Pizza):
    def do_pizza(self):
        return "I am Chicken pizza"


class PizzaDecorator(Pizza):
    def __init__(self, pizza_):
        self._pizza = pizza_

    @property
    def component(self):
        return self._pizza

    def do_pizza(self):
        return self._pizza.do_pizza()


class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza_):
        super().__init__(pizza_)

    def do_pizza(self):
        return f"{self._pizza.do_pizza()} + Cheese"


class PepperDecorator(PizzaDecorator):
    def __init__(self, pizza_):
        super().__init__(pizza_)

    def do_pizza(self):
        return f"{self._pizza.do_pizza()} + Pepper"


if __name__ == "__main__":
    tomato_pizza = TomatoPizza()
    chicken_pizza = ChickenPizza()
    print(tomato_pizza.do_pizza())
    print(chicken_pizza.do_pizza())

    pepper_tomato_pizza = PepperDecorator(tomato_pizza)
    pepper_chicken_pizza = PepperDecorator(chicken_pizza)
    print(pepper_tomato_pizza.do_pizza())
    print(pepper_chicken_pizza.do_pizza())

    cheese_pepper_tomato_pizza = CheeseDecorator(pepper_tomato_pizza)
    print(cheese_pepper_tomato_pizza.do_pizza())
