from abc import ABC, abstractmethod
from random import randint


class Species(ABC):
    """
    Species contains 2 types: Coffee and Longan.
    We defined 1 more type called NoneSpecies which is used to return a none type species in some cases.
    """
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
    """
    None type species
    """
    def get_name(self):
        pass


if __name__ == "__main__":
    species = None
    roll = randint(0, 2)
    if roll == 0:
        species = Coffee()  # Create Coffee species
    elif roll == 1:
        species = Longan()  # Create Longan species
    else:
        species = NoneSpecies()  # Create None type species
    if not isinstance(species, NoneSpecies):
        print(species.get_name())
    else:
        print("Invalid species")
