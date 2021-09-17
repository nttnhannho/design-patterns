from abc import ABC, abstractmethod
from random import randint


class Species(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Coffee(Species):
    def get_name(self):
        return "Coffee"


class Longan(Species):
    def get_name(self):
        return "Longan"


class NoneSpecies(Species):
    def get_name(self):
        pass


if __name__ == "__main__":
    species = None
    roll = randint(0, 2)
    if roll == 0:
        species = Coffee()
    elif roll == 1:
        species = Longan()
    else:
        species = NoneSpecies()
    if not isinstance(species, NoneSpecies):
        print(species.get_name())
    else:
        print("Invalid species")
