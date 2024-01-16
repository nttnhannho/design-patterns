import time
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print(f'{self.__class__.__name__} is handling request')


class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        if self.check_access():
            self.real_subject.request()
        self.log_access()

    def check_access(self):
        print(f'{self.__class__.__name__} is checking access')
        return True

    def log_access(self):
        print(f'{self.__class__.__name__} is logging access at:', time.time())


class Client:
    def __init__(self, request):
        self.request = request

    def call(self, subject):
        print(f'{self.__class__.__name__} is calling to {subject.__class__.__name__}')
        subject.request()


def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    client = Client('Request Access')
    client.call(proxy)


if __name__ == '__main__':
    main()
