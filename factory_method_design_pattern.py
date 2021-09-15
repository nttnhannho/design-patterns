from abc import ABC, abstractmethod
from random import randrange


class Species(ABC):
    @abstractmethod
    def show_name(self):
        pass


class Coffee(Species):
    def show_name(self):
        return "Coffee"


class Pepper(Species):
    def show_name(self):
        return "Pepper"


class Rubber(Species):
    def show_name(self):
        return "Rubber"


class Orange(Species):
    def show_name(self):
        return "Orange"


class Longan(Species):
    def show_name(self):
        return "Longan"


class Mango(Species):
    def show_name(self):
        return "Mango"


class Durian(Species):
    def show_name(self):
        return "Durian"


class SpeciesFactory(ABC):
    @abstractmethod
    def select_species(self):
        pass


class HighlandsFactory(SpeciesFactory):
    def select_species(self):
        num = randrange(3)
        if num == 0:
            return Coffee()
        if num == 1:
            return Pepper()
        if num == 2:
            return Rubber()


class MekongFactory(SpeciesFactory):
    count = 0

    def select_species(self):
        if MekongFactory.count == 0:
            MekongFactory.count += 1
            return Orange()
        if MekongFactory.count == 1:
            MekongFactory.count += 1
            return Mango()
        if MekongFactory.count == 2:
            MekongFactory.count += 1
            return Longan()
        if MekongFactory.count == 3:
            MekongFactory.count = 0
            return Durian()


if __name__ == "__main__":
    print("Highlands:")
    hls_factory = HighlandsFactory()
    for i in range(1, 13):
        species = hls_factory.select_species()
        print(f"The farmer number {i} received {species.show_name()}")

    print("*" * 50)

    print("Mekong:")
    mekong_factory = MekongFactory()
    for i in range(1, 13):
        species = mekong_factory.select_species()
        print(f"The farmer number {i} received {species.show_name()}")
