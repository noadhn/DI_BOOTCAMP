import random


def main():
    print("\nThis program generates random words from a given list,\n" +
          "and creates from them a sentence of you length's choice.\n")


def get_words_from_file():
    with open('random_words.txt', 'r') as random_words:
        words_list = [line.rstrip() for line in random_words]
        return words_list


def get_random_sentence(length):
    while length < 2 or length > 20:
        length = int(input("Please enter a number in the range:  "))
    words_list = get_words_from_file()
    sentence = []
    for each in range(length):
        word = random.choice(words_list)
        sentence.append(word)
    sentence = (' '.join(sentence)).lower()
    print(f"The non- sense sentence is:\n{sentence}")


main()
get_random_sentence(int(input("How many words in ur sentence my Lady? (must b in 2-20 range)  ")))
