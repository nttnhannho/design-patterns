from abc import ABC, abstractmethod
from enum import Enum


class Chair(ABC):
    @abstractmethod
    def create(self):
        pass


class PlasticChair(Chair):
    def create(self):
        return "Plastic chair"


class WoodChair(Chair):
    def create(self):
        return "Wood chair"


class Table(ABC):
    @abstractmethod
    def create(self):
        pass


class PlasticTable(Table):
    def create(self):
        return "Plastic table"


class WoodTable(Table):
    def create(self):
        return "Wood table"


class FurnitureAbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class PlasticFactory(FurnitureAbstractFactory):
    def create_chair(self):
        return PlasticChair()

    def create_table(self):
        return PlasticTable()


class WoodFactory(FurnitureAbstractFactory):
    def create_chair(self):
        return WoodChair()

    def create_table(self):
        return WoodTable()


class NoneMaterialType(FurnitureAbstractFactory):
    def create_chair(self):
        pass

    def create_table(self):
        pass


class MaterialType(Enum):
    PLASTIC = "Plastic"
    WOOD = "Wood"


class FurnitureFactory:
    @staticmethod
    def get_furniture(material_type_):
        switcher = {
            MaterialType.PLASTIC.value: PlasticFactory(),
            MaterialType.WOOD.value: WoodFactory()
        }
        return switcher.get(material_type_, NoneMaterialType())


if __name__ == "__main__":
    factory = FurnitureFactory.get_furniture(MaterialType.PLASTIC.value)
    chair = factory.create_chair()
    print(chair.create())
    table = factory.create_table()
    print(table.create())

    factory = FurnitureFactory.get_furniture(MaterialType.WOOD.value)
    chair = factory.create_chair()
    print(chair.create())
    table = factory.create_table()
    print(table.create())

    factory = FurnitureFactory.get_furniture("null")
    if not isinstance(factory, NoneMaterialType):
        chair = factory.create_chair()
        print(chair.create())
        table = factory.create_table()
        print(table.create())
    else:
        print("Invalid material")
