class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age)*10

    def fight(self, other_dog):
        other_dog_weight = other_dog.weight
        other_dog_age = other_dog.age
        other_dog_speed = (other_dog_weight / other_dog_age)*10
        if self.run_speed() > other_dog_speed:
            return "won the fight"
        else:
            return "lost the fight"


dog1 = Dog('rex', 12, 13)
dog2 = Dog('yoko', 6, 32)
dog3 = Dog('bianca', 9, 4)

print(f"{dog1.bark()}\n{dog1.name}'s speed is {dog1.run_speed()} mph\n{dog1.name} {dog1.fight(dog2)} against {dog2.name}\n")
print(f"{dog2.bark()}\n{dog2.name}'s speed is {dog2.run_speed()} mph\n{dog2.name} {dog1.fight(dog3)} against {dog3.name}\n")
print(f"{dog3.bark()}\n{dog3.name}'s speed is {dog3.run_speed()} mph\n{dog3.name} {dog1.fight(dog1)} against {dog1.name}")
