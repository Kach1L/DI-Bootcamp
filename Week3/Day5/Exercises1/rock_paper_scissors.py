import game

def get_user_menu_choice():
    print("(g) Play a new game")
    print("(x) Show scores and quit\n:") 
    choice = input()
    return input

def print_results(results):
    return results

def main():
    if choice == 'g':
        play()
    else:
        print_results(get_game_results())
    # Don't know how to implement the yellow underlined code from the game py file. 