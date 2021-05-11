class Human:

    def __init__(self, name):
        self.name = name

    def my_name(self):
        print(f"My name is {self.name}.")

    @staticmethod
    def voice():
        print("I have a great voice")

    def __add__(self, other):
        if isinstance(other, Human):
            print("New Human")
        elif isinstance(other, Alien):
            print("Predator")


class Alien:

    def __init__(self):
        self.affront = "Fuck you"

    def my_name(self):
        print(f"{self.affront}, I don't have any name")

    @staticmethod
    def voice():
        print("asoidjf;sijdd")

    def __add__(self, other):
        if isinstance(other, Alien):
            return "Agg of an alien"
        elif isinstance(other, Human):
            return "*crying*"





human1 = Human("Nick")
human2 = Human("Stas")

alien1 = Alien()
alien2 = Alien()

human1 + human2
alien1 + alien2
human2 + alien1
alien1 + human2

# for i in (human1, alien1):
#     i.my_name()
#     i.voice()
