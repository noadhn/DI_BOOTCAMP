import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
			 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_stars = []
star = "*"
user_guess = ""


print(word)


def replace_stars(word):
	for letter in word:
		word_stars.append(star)
	print(word_stars)


replace_stars(word)


def check_user_guess(num_guessed: int):
	if "*" in word_stars:
		if num_guessed < 5:
			user_guess = input("\nPlease guess a letter: ")
			flag = False
			for counter, letter in enumerate(word):

				if user_guess == letter:
					word_stars[counter] = user_guess
					flag = True

			if flag == False:
				num_guessed += 1

			print(word_stars)
			return num_guessed
	else:
		return

num_guessed = 0



while num_guessed < 5:
	num_guessed = check_user_guess(num_guessed)

if num_guessed == 5:
	print('you lose')
else:
	print('you won')
