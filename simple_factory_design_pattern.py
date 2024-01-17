from abc import ABC


class Sneaker(ABC):
    def __repr__(self):
        return f'{self.__class__.__name__}'


class Nike(Sneaker):
    pass


class Puma(Sneaker):
    pass


class SneakerFactory:
    @staticmethod
    def create_type(sneaker_type):
        sneakers = {
            'Nike': Nike,
            'Puma': Puma,
        }

        return sneakers.get(sneaker_type)()


def main():
    sneaker = SneakerFactory.create_type('Nike')
    print(sneaker)


if __name__ == '__main__':
    main()
