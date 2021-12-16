import random


def random_calculate(num_1):
    num_2 = random.randint(1, 101)
    if num_1 == num_2:
        print("HEY WHAT A PIECE OF CHANCE")
    else:
        print("Both numbers are: "+ str(num_1)+ " and "+ str(num_2)+ " ,MAYBE NEXT TIME")

random_calculate(random.randint(1,101))