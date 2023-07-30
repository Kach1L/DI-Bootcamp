import rock_paper_scissors
import random

class Game:
    def __init__(self):
        self.result = {
            "draw" : 0,
            "win" : 0,
            "loss" : 0
        }  
    
    def get_user_item(self):
        game_list=['rock','paper','scissors']
        try:
            user_choice=input('Select an item rock/paper/scissors: ')
            if user_choice not in game_list:
                raise Exception("problem")
        except:
            print('Answer needs to be rock, paper, and scissors')
        else:
            print(f'You selected {user_choice}')
            return (user_choice) 
    
    def get_computer_item(self):
        game_list=['rock','paper','scissors']
        comp_choice = random.choice(game_list)
        print(f'The computer selected {comp_choice}')
        return comp_choice
    
    def get_game_result(self, user_item, computer_item):
        game_list=['rock','paper','scissors']
        if user_item == computer_item:
            self.result["draw"] += 1
            print(f'Result: you drew')
        elif (user_item == game_list[0] and computer_item == game_list[1] or
        user_item == game_list[1] and computer_item == game_list[2] or user_item == game_list[2] and computer_item == game_list[0]):
            self.result["loss"] += 1
            print(f'Result: you lost')
        elif (user_item == game_list[0] and computer_item == game_list[2] or user_item == game_list[1] and computer_item == game_list[0] or user_item == game_list[2] and computer_item == game_list[1]):
            self.result["win"] += 1
            print(f'Result: you win')
            
    def play(self):
        user = self.get_user_item()
        comp = self.get_computer_item()
        self.get_game_result(user,comp)

game1=Game()
game1.play()
