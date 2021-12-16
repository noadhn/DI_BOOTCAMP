class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sphynx(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Sphynx('Pharaoe', 16)
cat2 = Sphynx('Neferttiti', 1)
cat3 = Sphynx('Egy', 22)
my_cats = [cat1, cat2, cat3]
my_pets = Pets(my_cats)
print(my_pets.walk())
