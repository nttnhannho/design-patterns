import copy
import time
from abc import ABC, abstractmethod
from datetime import datetime


class NPCPrototype(ABC):
    def __init__(self):
        time.sleep(3)  # Mocking an expensive call
        self.age = None
        self.height = None
        self.defense = None
        self.attack = None
        self.heal = 0
        self.talents = []

    def do_heal(self):
        self.heal += 1

    @abstractmethod
    def clone(self):
        pass


class ShopkeeperNPC(NPCPrototype):
    def __init__(self, age, height, defense, attack):
        super().__init__()
        self.age = age
        self.height = height
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)


class WarriorNPC(NPCPrototype):
    def __init__(self, age, height, defense, attack):
        super().__init__()
        self.age = age
        self.height = height
        self.defense = defense
        self.attack = attack
        self.stamina = 60

    def clone(self):
        return copy.copy(self)  # Be careful with shallow copy


def main():
    print('Creating Shopkeeper NPCs without using prototype...')
    start = datetime.now()
    for _ in range(5):
        shopkeeper = ShopkeeperNPC(age=20, height=180, defense=200, attack=200)
    print('Finished creating Shopkeeper NPCs without using prototype with:', datetime.now() - start)  # Created in 15.008078

    print('*' * 100)

    print('Creating Shopkeeper NPCs using prototype...')
    start = datetime.now()
    shopkeeper_template = ShopkeeperNPC(age=20, height=180, defense=200, attack=200)
    for _ in range(5):
        shopkeeper_clone = shopkeeper_template.clone()
    print('Finished creating Shopkeeper NPCs using prototype with:', datetime.now() - start)  # Created in 03.002450

    print('*' * 100)

    shopkeeper_test = ShopkeeperNPC(age=20, height=180, defense=200, attack=200)
    aris = shopkeeper_test.clone()
    bob = shopkeeper_test.clone()
    bob.do_heal()
    bob.talents.append('invisibility')
    print(f'Aris heal = {aris.heal}, Bob heal = {bob.heal}')
    print(f'Aris talents = {aris.talents}, Bob talents = {bob.talents}')
    print(id(aris), id(bob))

    warrior_test = WarriorNPC(age=20, height=180, defense=200, attack=200)
    chiel = warrior_test.clone()
    dig = warrior_test.clone()
    dig.do_heal()
    dig.talents.append('immortality')
    print(f'Chiel heal = {chiel.heal}, Dig heal = {dig.heal}')
    print(f'Chiel talents = {chiel.talents}, Dig talents = {dig.talents}')
    print(id(chiel), id(dig))


if __name__ == '__main__':
    main()
