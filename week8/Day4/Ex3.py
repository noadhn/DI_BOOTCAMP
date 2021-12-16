from Ex2 import Dog
import random


class PetDog(Dog):

    def __init__(self, name, age, weight, trained=False):
        self.trained = trained
        super().__init__(name, age, weight)

    def train(self):
        print(self.bark())
        PetDog.trained = True

    def play(self, *other_dogs: str):
        dogs = list()
        dogs.extend(other_dogs)
        return f"{', '.join(map(str, dogs))} all play together"

    def do_a_trick(self):
        tricks = ("does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead")
        rand = random.Random()
        if self.trained:
            trick = rand.choice(tricks)
            return f"{self.name} {trick}"


dog1 = PetDog('Rockie', 6, 8, True).do_a_trick()
print(dog1)
