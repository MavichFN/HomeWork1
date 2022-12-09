class Pet:
    def __init__(self, name):
        self.name = name
    class Animals:
        def __init__(self, Dog, Cat, Parrot):
            self.Dog = Dog
            self.Cat = Cat
            self.Parrot = Parrot
        def add_animals(self, Pet):
            self.Animals.append(Pet)

Characteristic = ("Animals", "Name")
# Characteristic.add_animals(Pet("Graf"))
# Characteristic.add_animals(Pet("Max"))
# Characteristic.add_animals(Pet("Blue"))
# Characteristic.add_animals(Pet("Lucky"))
# Characteristic.add_animals(Pet("Awful"))
Characteristic.print_add_animals()

