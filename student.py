from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    @abstractmethod
    def display(self):
        pass

    def __init__(self, name, age):
        self.name = name
        self.__age = age          # Encapsulation

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age