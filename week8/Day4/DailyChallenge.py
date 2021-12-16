import random

random = random.Random()
boolean = (True, False)
chromosome = ""
dna = []
i = 0
while i < 10:
    chromosome = [random.choice(boolean) for i in range(10)]
    dna.append(chromosome)
    i += 1

print("\n".join(map(str, dna)))


class Organism:
    def __init__(self, environment=int):
        self.environment = environment

    def if_mutate(self, environment):
        if environment == 0:
            return dna
        # else:

# probability of DNA to change is 20% ->
# probability of chromosome to mutate is 20% * 50%
# x * 0.5


first = Organism().if_mutate(0)
print("\n".join(map(str, first)))
