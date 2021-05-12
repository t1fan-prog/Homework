class Animal:

    @staticmethod
    def talk():
        return "I am animal and I can talk"


class Cat(Animal):

    @staticmethod
    def talk():
        return "Meow"


class Dog(Animal):

    @staticmethod
    def talk():
        return "Woof"


some_cat = Cat()
some_dog = Dog()


def talk_animal(animal):
    if isinstance(animal, Cat) or isinstance(animal, Dog):
        print(animal.talk())
    else:
        print("Some animal is talking")
