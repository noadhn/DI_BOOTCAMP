class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_oldest(cats):
    oldest_cat = 0
    for cat in cats:
        if cat.age > oldest_cat:
            oldest_cat = cat.age
            oldest_cat_name = cat.name
    print("The oldest cat is " + str(oldest_cat_name))


cat1 = Cat('Catty', 12)
cat2 = Cat('Motek', 4)
cat3 = Cat('Moriki', 6)
cats = [cat1, cat2, cat3]


find_oldest(cats)
