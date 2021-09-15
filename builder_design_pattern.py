from abc import ABC, abstractmethod


class Student:
    def __init__(self, id_, firstname_, lastname_, dob_, address_, phone_):
        self.__id = id_
        self.__firstname = firstname_
        self.__lastname = lastname_
        self.__dob = dob_
        self.__address = address_
        self.__phone = phone_

    def __str__(self):
        return f"{self.__id}, {self.__firstname}, {self.__lastname}, {self.__dob}, {self.__address}, {self.__phone}"


class StudentBuilder(ABC):
    @abstractmethod
    def set_id(self, id_):
        pass

    @abstractmethod
    def set_firstname(self, firstname_):
        pass

    @abstractmethod
    def set_lastname(self, lastname_):
        pass

    @abstractmethod
    def set_dob(self, dob_):
        pass

    @abstractmethod
    def set_address(self, address_):
        pass

    @abstractmethod
    def set_phone(self, phone_):
        pass

    @abstractmethod
    def build(self):
        pass


class StudentConcreteBuilder(StudentBuilder):
    def __init__(self):
        self.__id = None
        self.__firstname = None
        self.__lastname = None
        self.__dob = None
        self.__address = None
        self.__phone = None

    def set_id(self, id_):
        self.__id = id_
        return self

    def set_firstname(self, firstname_):
        self.__firstname = firstname_
        return self

    def set_lastname(self, lastname_):
        self.__lastname = lastname_
        return self

    def set_dob(self, dob_):
        self.__dob = dob_
        return self

    def set_address(self, address_):
        self.__address = address_
        return self

    def set_phone(self, phone_):
        self.__phone = phone_
        return self

    def build(self):
        return Student(self.__id, self.__firstname, self.__lastname, self.__dob, self.__address, self.__phone)


if __name__ == "__main__":
    student_builder1 = StudentConcreteBuilder()\
        .set_id(1)\
        .set_firstname("Nhan")\
        .set_lastname("Nguyen")
    student1 = student_builder1.build()
    print(student1)

    student_builder2 = StudentConcreteBuilder()\
        .set_id(2)\
        .set_firstname("Tom")\
        .set_lastname("Jerry")\
        .set_phone("0123")
    student2 = student_builder2.build()
    print(student2)
