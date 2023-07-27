import anagram_checker

def get_anagram_menu():
    inp1 =input("(g) Input a word")
    print("(x) Exit\n:") 
    choice1 = inp1
    def main():
        if choice1 == 'g':
            try:
                inp2 = input("(g) Input a word")
            except:
                ValueError('Only alphabetic characters are allowed. No numbers or special characters.')
            else:
                print('Now validating user input........')
            get_anagram_menu()
        else:
            StopIteration
def is_valid_word2(self, word):
    word = input('write a word')
    word(word.lower())
    
    for i in word:
      anagram = i + anagram( word - {i} ) # remove the char from its position in the string
      print(anagram)
      print(anagram_checker)
            
        