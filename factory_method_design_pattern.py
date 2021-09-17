from abc import ABC, abstractmethod


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


class NoneSpecies(Species):
    def show_name(self):
        pass


class SpeciesFactory:
    @staticmethod
    def get_species(type_):
        switcher = {
            "Coffee": Coffee(),
            "Pepper": Pepper(),
            "Rubber": Rubber(),
            "Orange": Orange(),
            "Longan": Longan(),
            "Mango": Mango(),
            "Durian": Durian()
        }
        return switcher.get(type_, NoneSpecies())


if __name__ == "__main__":
    species = SpeciesFactory.get_species("Coffee")
    print(species.show_name())
    species = SpeciesFactory.get_species("null")
    if not isinstance(species, NoneSpecies):
        print(species.show_name())
    else:
        print("Invalid species")
