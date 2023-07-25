import googletrans

french_words= "Bonjour : Au revoir : Bienvenue : A bientôt"

translator = googletrans.Translator

trans1 = googletrans.Translator.detect(french_words,'')
print(trans1)

