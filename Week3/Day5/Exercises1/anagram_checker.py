from collections import defaultdict
import anagrams

class AnagramChecker:
    def __init__(self):
        with open('temp.txt') as temp:
            tempo = temp.readlines
    
    def is_valid_word(self, word):
        word = input('write a word')
        print(f"YOUR WORD : '{word}'")
        word(word.lower())
        return f'this is a valid English word'
    
    def get_anagrams(word):
        temp = word2(str)
        word2 = input('write a word for anagram focus')
        for i in word2:
            temp[str(sorted(i))].append(i)
            res = list(temp.values())
            # print result
            print("Anagrams for your word : " + list(res))
    
    