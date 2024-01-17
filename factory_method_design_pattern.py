from abc import ABC, abstractmethod


class Transportation(ABC):
    def __init__(self, name, doors, price, customer_info=None):
        self.name = name
        self.doors = doors
        self.price = price
        self.customer_info = customer_info

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, doors={self.doors}, price={self.price}, customer_info={self.customer_info})'


class Car(Transportation):
    def __init__(self, name='XL7', doors='4', price='600.000.000 VND', customer_info=None):
        super().__init__(name, doors, price, customer_info)


class ServiceLogisticsFactory(ABC):
    transportation_class = None

    @classmethod
    def get_transport(cls, customer_info):
        return cls.transportation_class(customer_info=customer_info)


class CarService(ServiceLogisticsFactory):
    transportation_class = Car


class Truck(Transportation):
    def __init__(self, name='Container 2024', doors='2', price='3.000.000.000 VND', customer_info=None):
        super().__init__(name, doors, price, customer_info)


class TrucService(ServiceLogisticsFactory):
    transportation_class = Truck


def main():
    car_service = CarService()
    print(car_service.get_transport(customer_info={'name': 'nhan'}))
    truck_service = TrucService()
    print(truck_service.get_transport(customer_info={'name': 'futaro'}))


if __name__ == '__main__':
    main()
