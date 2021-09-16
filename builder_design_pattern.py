from abc import ABC, abstractmethod


class House:
    def __init__(self, basement_, structure_, roof_, interior_):
        self.__basement = basement_
        self.__structure = structure_
        self.__roof = roof_
        self.__interior = interior_

    def __str__(self):
        return f"{self.__basement}, {self.__structure}, {self.__roof}, {self.__interior}"

    @property
    def basement(self):
        return self.__basement

    @basement.setter
    def basement(self, value_):
        self.__basement = value_

    @property
    def structure(self):
        return self.__structure

    @structure.setter
    def structure(self, value_):
        self.__structure = value_

    @property
    def roof(self):
        return self.__roof

    @roof.setter
    def roof(self, value_):
        self.__roof = value_

    @property
    def interior(self):
        return self.__interior

    @interior.setter
    def interior(self, value_):
        self.__interior = value_


class HouseBuilder(ABC):
    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def get_house(self):
        pass


class IglooHouseBuilder(HouseBuilder):
    def __init__(self):
        self.__basement = None
        self.__structure = None
        self.__roof = None
        self.__interior = None

    def build_basement(self):
        self.__basement = "Ice Bars"

    def build_structure(self):
        self.__structure = "Ice Blocks"

    def build_roof(self):
        self.__roof = "Ice Dome"

    def build_interior(self):
        self.__interior = "Ice Carvings"

    def get_house(self):
        return House(self.__basement, self.__structure, self.__roof, self.__interior)


class TipiHouseBuilder(HouseBuilder):
    def __init__(self):
        self.__basement = None
        self.__structure = None
        self.__roof = None
        self.__interior = None

    def build_basement(self):
        self.__basement = "Wooden Poles"

    def build_structure(self):
        self.__structure = "Wood and Ice"

    def build_roof(self):
        self.__roof = "Wood, caribou and seal skins"

    def build_interior(self):
        self.__interior = "Fire Wood"

    def get_house(self):
        return House(self.__basement, self.__structure, self.__roof, self.__interior)


class HouseDirector:
    def __init__(self, housebuilder_):
        self.__housebuilder = housebuilder_

    def get_house(self):
        return self.__housebuilder.get_house()

    def build_full_house(self):
        self.__housebuilder.build_basement()
        self.__housebuilder.build_structure()
        self.__housebuilder.build_roof()
        self.__housebuilder.build_interior()

    def build_basement_only(self):
        self.__housebuilder.build_basement()

    def build_structure_only(self):
        self.__housebuilder.build_structure()

    def build_roof_only(self):
        self.__housebuilder.build_roof()

    def build_interior_only(self):
        self.__housebuilder.build_interior()


if __name__ == "__main__":
    igloo_house_builder = IglooHouseBuilder()
    house_director = HouseDirector(igloo_house_builder)
    house_director.build_full_house()
    print(house_director.get_house())
