# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # геттер имени
    def get_name(self):
        return self.__name

    # сеттер имени
    def set_name(self, name):
        self.__name = name

    # геттер возраста
    def get_age(self):
        return self.__age

    # сеттер возраста
    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")


# класс Dog
class Dog(Animal):
    def make_sound(self):
        print("Гав гав")


# класс Cat
class Cat(Animal):
    def make_sound(self):
        print("Мяу")


# создаем объекты
dog = Dog("Rex", 3)
kitty = Cat("Barsik", 1)

# вывод звуков
dog.make_sound()
kitty.make_sound()

# изменение возраста через сеттер
kitty.set_age(2)

# вывод возраста через геттер
print(kitty.get_age())