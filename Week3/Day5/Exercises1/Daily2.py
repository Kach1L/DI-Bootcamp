import random
# What is a class? A class is the base of a group of functions used to make an interface.
# What is an instance? Is the occupying values you give a parameter of a function.
# What is encapsulation? Is when you hide code which would look packed if left unhidden.
# What is abstraction? the a process of handling dynamics by hiding unnecessary information from the user.
# What is inheritance? It's when parameters and function are accessed by a sub class in oop.
# What is multiple inheritance? Its when parameters and function are accessed by a multiple sub class in oop.
# What is polymorphism? It's when an object is being changed in different ways.
# What is method resolution order or MRO? the sequence in which a method is searched for in a classes hierarchy

class Card:
    def __init__(self):
        suit = ('Hearts','Diamonds','Clubs','Spades')
        value = (('A',2,3,4,5,6,7,8,9,10,'J','Q','K'))
        
class Deck:
    def __init___(self,deck_of_cards):
        self.deck_of_cards = deck_of_cards
        print(f'Here are your deck of cards:\n{deck_of_cards}')
        
        rand_deck=deck_of_cards[:]
        random.shuffle(rand_deck)
        print(rand_deck)
    
    def deal(self,deck_of_cards):
        deal_card = input('choose a card like this H1:\n')
        self.deck_of_cards - self.deck_of_cards[deal_card]
    
play1 = Deck()
play1.__init__('HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK', 'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK', 'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK', 'SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK')
play1.deal()
        
        
        
        
    
            
