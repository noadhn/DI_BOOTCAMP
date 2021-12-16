
class Farm:
	def __init__(self, name):
		self.name = name
		self.animals = {}
		print(f"{self.name}'s farm")

	def add_animal(self, animal: str, quantity: int = 1):
		self.animals[animal] = self.animals.get(animal, 0) + quantity
		print(f"{animal} : {self.animals[animal]}")

		#for animal_name, animal_count in self.animals.items():
			#print(f"{animal}: {quantity}")

	def get_animal_types(self):
		print(sorted(self.animals.keys()))


mcdonalds = Farm("Mcdonald")
mcdonalds.add_animal("cow", 5)
mcdonalds.add_animal("sheep")
mcdonalds.add_animal("sheep")
mcdonalds.add_animal("goat", 12)
#print(mcdonalds.animals)
