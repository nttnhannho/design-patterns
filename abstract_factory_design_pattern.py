from abc import ABC, abstractmethod
from enum import Enum


class Chair(ABC):
    """
    Chair has 2 types: Plastic and Wood.
    """
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
    """
    Table has 2 types: Plastic and Wood.
    """
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
    """
    FurnitureAbstractFactory supports to create chair and table.
    FurnitureAbstractFactory has 2 types of material: PlasticFactory and WoodFactory.
    We also defined a none type material. This one will be mentioned clearly in Null object design pattern.
    """
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
    """
    The factory decides which factory will be used to create chair and table.
    """
    @staticmethod
    def get_furniture(material_type_):
        switcher = {
            MaterialType.PLASTIC.value: PlasticFactory(),
            MaterialType.WOOD.value: WoodFactory()
        }
        return switcher.get(material_type_, NoneMaterialType())


if __name__ == "__main__":
    factory = FurnitureFactory.get_furniture(MaterialType.PLASTIC.value)  # Create plastic factory
    chair = factory.create_chair()  # Create plastic chair
    print(chair.create())
    table = factory.create_table()  # Create plastic table
    print(table.create())

    factory = FurnitureFactory.get_furniture(MaterialType.WOOD.value)  # Create wood factory
    chair = factory.create_chair()  # Create wood chair
    print(chair.create())
    table = factory.create_table()  # Create wood table
    print(table.create())

    factory = FurnitureFactory.get_furniture("null")  # Create none type factory
    if not isinstance(factory, NoneMaterialType):
        chair = factory.create_chair()
        print(chair.create())
        table = factory.create_table()
        print(table.create())
    else:
        print("Invalid material")
