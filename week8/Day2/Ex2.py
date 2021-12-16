class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(self.name + " goes woof!")

    def jump(self):
        print(self.name + " jumps " + str(int(self.height)*2) + " cm")

        if davids_dog.height > sarahs_dog.height:
            print("The biggest dog is " + str(davids_dog.name))
        else:
            print("The biggest dog is " + str(sarahs_dog.name))


davids_dog = Dog('Rex', 50)
sarahs_dog = Dog('Teacup', 20)
print(f"David's dog's name is {davids_dog.name} and it is {davids_dog.height} cm height.")
Dog.bark(davids_dog)
Dog.jump(davids_dog)
print(f"sarah's dog name is {sarahs_dog.name} and it is {sarahs_dog.height} cm height.")
Dog.bark(sarahs_dog)
Dog.jump(sarahs_dog)
