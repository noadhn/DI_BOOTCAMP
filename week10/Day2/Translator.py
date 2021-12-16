from translate import Translator

translator = Translator(from_lang="French", to_lang="English")
translation = translator.translate

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
french_to_english = {}
for every in french_words:
    french_to_english[every] = translation(every)


print(french_to_english)
