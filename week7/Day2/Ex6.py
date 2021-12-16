magicians = ["David Abbot", "David Acer", "Curtis Adams", "Ivan Amodei", "Jason Alexander"]
magicians_new = []

def show_magicians(magicians):
    for each in magicians:
        print(each)


def make_great(magicians):
    i = 0
    for each in magicians:
        magicians_new.append("the Great " + each)
    for each in magicians:
        magicians[i] = magicians_new[i]
        i += 1
    return magicians


make_great(magicians)
show_magicians(magicians)
