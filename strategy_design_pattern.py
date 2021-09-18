from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    """
    Operation contains 4 types: addition, subtraction, multiplication, division.
    """
    @abstractmethod
    def operate(self, num_a, num_b):
        pass


class Addition(OperationStrategy):
    """
    Addition
    """
    def operate(self, num_a, num_b):
        return num_a + num_b


class Subtraction(OperationStrategy):
    """
    Subtraction
    """
    def operate(self, num_a, num_b):
        return num_a - num_b


class Multiplication(OperationStrategy):
    """
    Multiplication
    """
    def operate(self, num_a, num_b):
        return num_a * num_b


class Division(OperationStrategy):
    """
    Division
    """
    def operate(self, num_a, num_b):
        if num_b == 0:
            raise ZeroDivisionError
        return num_a / num_b


class OperationContext:
    """
    Defines which operation will be used and be able to modify the operation in runtime.
    """
    def __init__(self, strategy_):
        self.__strategy = strategy_

    def __str__(self):
        return self.__strategy.__class__.__name__

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, value_):
        """
        Set which operation will be used
        :param value_: operation
        :return: None
        """
        self.__strategy = value_

    def do_operation(self, num_a, num_b):
        """
        Do the operation on number a and b
        :param num_a: number a
        :param num_b: number b
        :return: result of the operation on number a and b
        """
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
