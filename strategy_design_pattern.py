from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def operate(self, num_a, num_b):
        pass


class Addition(OperationStrategy):
    def operate(self, num_a, num_b):
        return num_a + num_b


class Subtraction(OperationStrategy):
    def operate(self, num_a, num_b):
        return num_a - num_b


class Multiplication(OperationStrategy):
    def operate(self, num_a, num_b):
        return num_a * num_b


class Division(OperationStrategy):
    def operate(self, num_a, num_b):
        if num_b == 0:
            raise ZeroDivisionError
        return num_a / num_b


class OperationContext:
    def __init__(self, strategy_):
        self.__strategy = strategy_

    def __str__(self):
        return self.__strategy.__class__.__name__

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, value_):
        self.__strategy = value_

    def do_operation(self, num_a, num_b):
        return self.__strategy.operate(num_a, num_b)


if __name__ == "__main__":
    a = 10
    b = 5

    try:
        context = OperationContext(Addition())
        print(f"{context} = {context.do_operation(a, b)}")

        context.strategy = Subtraction()
        print(f"{context} = {context.do_operation(a, b)}")

        context.strategy = Multiplication()
        print(f"{context} = {context.do_operation(a, b)}")

        context.strategy = Division()
        print(f"{context} = {context.do_operation(a, b)}")
    except ZeroDivisionError:
        print(f"Division = Can not divide by zero !!")
