from abc import ABC, abstractmethod


class Pizza(ABC):
    """
    Pizza has 2 types: Tomato and Chicken pizza.
    """
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
    """
    Pizza topping has 2 types: Cheese and Pepper.
    So, we can add Pepper and Cheese toppings for Tomato and Chicken pizzas.
    """
    def __init__(self, pizza_):
        self.__pizza = pizza_

    @property
    def pizza(self):
        return self.__pizza

    def do_pizza(self):
        return self.__pizza.do_pizza()


class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza_):
        super().__init__(pizza_)

    def do_pizza(self):
        return f"{self.pizza.do_pizza()} + Cheese"


class PepperDecorator(PizzaDecorator):
    def __init__(self, pizza_):
        super().__init__(pizza_)

    def do_pizza(self):
        return f"{self.pizza.do_pizza()} + Pepper"


if __name__ == "__main__":
    tomato_pizza = TomatoPizza()  # Create tomato pizza
    chicken_pizza = ChickenPizza()  # Create chicken pizza
    print(tomato_pizza.do_pizza())
    print(chicken_pizza.do_pizza())

    pepper_tomato_pizza = PepperDecorator(tomato_pizza)  # Create pepper tomato pizza
    pepper_chicken_pizza = PepperDecorator(chicken_pizza)  # Create pepper chicken pizza
    print(pepper_tomato_pizza.do_pizza())
    print(pepper_chicken_pizza.do_pizza())

    cheese_pepper_tomato_pizza = CheeseDecorator(pepper_tomato_pizza)  # Create cheese pepper tomato pizza
    print(cheese_pepper_tomato_pizza.do_pizza())
