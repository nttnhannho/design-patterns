from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.__parts = []

    def build_part(self, part_):
        self.__parts.append(part_)

    def __str__(self):
        return ', '.join(self.__parts)


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
    def build(self):
        pass


class IglooHouseBuilder(HouseBuilder):
    def __init__(self):
        self.__reset()

    def __reset(self):
        self.__house = House()

    def build_basement(self):
        self.__house.build_part("Ice Bars")

    def build_structure(self):
        self.__house.build_part("Ice Blocks")

    def build_roof(self):
        self.__house.build_part("Ice Dome")

    def build_interior(self):
        self.__house.build_part("Ice Carvings")

    def build(self):
        house_ = self.__house
        self.__reset()
        return house_


class TipiHouseBuilder(HouseBuilder):
    def __init__(self):
        self.__reset()

    def __reset(self):
        self.__house = House()

    def build_basement(self):
        self.__house.build_part("Wooden Poles")

    def build_structure(self):
        self.__house.build_part("Wood and Ice")

    def build_roof(self):
        self.__house.build_part("Wood, caribou and seal skins")

    def build_interior(self):
        self.__house.build_part("Fire Wood")

    def build(self):
        house_ = self.__house
        self.__reset()
        return house_


class HouseDirector:
    def __init__(self):
        self.__housebuilder = None

    @property
    def housebuilder(self):
        return self.__housebuilder

    @housebuilder.setter
    def housebuilder(self, value_):
        self.__housebuilder = value_

    def get_house(self):
        return self.__housebuilder.build()

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
    house_director = HouseDirector()

    print("Igloo house:")
    igloo_house_builder = IglooHouseBuilder()
    house_director.housebuilder = igloo_house_builder
    house_director.build_full_house()
    house = house_director.get_house()
    print(f"Full house: {house}")

    house_director.build_basement_only()
    house = house_director.get_house()
    print(f"Basement only house: {house}")

    house_director.build_structure_only()
    house = house_director.get_house()
    print(f"Structure only house: {house}")

    house_director.build_roof_only()
    house = house_director.get_house()
    print(f"Roof only house: {house}")

    house_director.build_interior_only()
    house = house_director.get_house()
    print(f"Interior only house: {house}")

    print("*" * 50)

    print("Tipi house:")
    tipi_house_builder = TipiHouseBuilder()
    house_director.housebuilder = tipi_house_builder
    house_director.build_full_house()
    house = house_director.get_house()
    print(f"Full house: {house}")

    house_director.build_basement_only()
    house = house_director.get_house()
    print(f"Basement only house: {house}")

    house_director.build_structure_only()
    house = house_director.get_house()
    print(f"Structure only house: {house}")

    house_director.build_roof_only()
    house = house_director.get_house()
    print(f"Roof only house: {house}")

    house_director.build_interior_only()
    house = house_director.get_house()
    print(f"Interior only house: {house}")
