from collections import Counter
import heapq
import os
class Text:
    def __init__(self,string):
        self.string = string
    
    def printer(self,string):
        return string
    
    def frequency(self,string):
        freq = Counter(string.split()).most_common()
        print('These are all the frequencies of the words in the sentence:')
        return freq
    
    def mostFrequentWord(self,test_list):
        all_words = [sub.split() for sub in test_list]
        word_counts = Counter(word for sublist in all_words for word in sublist)
        return heapq.nlargest(1, word_counts, key=word_counts.get)[0]
    
    @classmethod
    def retext(cls,text):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        with open(text,'r') as f:
            all_lines = f.readlines()
            print(str(all_lines))
            file = (path+r"\the_stranger.txt")
            print(file)     
        
        
text1 = Text('A good book would sometimes cost as much as a good house.')
print(text1.printer('A good book would sometimes cost as much as a good house.'))
print(text1.frequency('A good book would sometimes cost as much as a good house.'))
print(text1.mostFrequentWord('A good book would sometimes cost as much as a good house'))


