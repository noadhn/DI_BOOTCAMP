from itertools import groupby
from operator import itemgetter


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animal(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        counter = 1
        print(sorted(self.animals))
        for letter, animals in groupby(sorted(self.animals), key=itemgetter(0)):
            print(str(counter), ":")
            counter += 1
            for animal in animals:
                print(animal)


ramat_gan_safari = Zoo('Ramat Gan Safary')
ramat_gan_safari.add_animal('zebra')
ramat_gan_safari.add_animal('alpa')
ramat_gan_safari.add_animal('girrafe')
ramat_gan_safari.add_animal('zzr')
ramat_gan_safari.sort_animals()
