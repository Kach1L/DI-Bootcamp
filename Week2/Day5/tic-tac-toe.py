# Tic-tac-toe Game
# Function 1 Ex 1
def play():
    start = input('Write "Play" to Start\n')
    if start == "Play":
        display_board()
    else:
        pass
play()

space = [i for i in range(1,10)]
def display_board():
    print("❌⭕GAME\nHere is the board")
    board = ''
    first = ''
# for i in range(0,1):
    # for r in space:
        # if i % 2 == 0:
    board += '  ---   ---   --- '
        # else:
    board += f'\n|  {space[0]}  |  {space[1]}  |  {space[2]}  |   '
    board += '\n  ---   ---   --- '
    board += f'\n|  {space[3]}  |  {space[4]}  |  {space[5]}  |   '
    board += '\n  ---   ---   --- '
    board += f'\n|  {space[6]}  |  {space[7]}  |  {space[8]}  |   '
    board += '\n'
    board += '  ---   ---   --- '
    print(board)    
display_board()



# Function 2 Ex 2
def player_input(player, other):
    global space
    i = 0
    while i <= 3:
        move1 = 'X'
        move2 = 'O'
        turn1 = int(input('Player 1, choose 1-9\n'))
        space[turn1-1] = move1
        display_board()
        turn2 = int(input('Player 2, choose 1-9\n'))
        space[turn2-1] = move2
        display_board()
        i += 1
    print('No Winner, Play Again')
    if i == 2 or i == 3:
        check_win()
    elif i == 2 or i == 3:
        check_win()
        
        
    
player_input('player1', 'player2')



# Function 3 Ex 3
def check_win():
    if space[0] and space[1] and space[2] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[0] and space[1] and space[2] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[3] and space[4] and space[5] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[3] and space[4] and space[5] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[6] and space[7] and space[8] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[6] and space[7] and space[8] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[0] and space[4] and space[8] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[0] and space[4] and space[8] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[2] and space[4] and space[6] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[2] and space[4] and space[6] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[0] and space[3] and space[6] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[0] and space[3] and space[6] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[1] and space[4] and space[7] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[1] and space[4] and space[7] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    elif space[2] and space[5] and space[8] == 'X':
        print('Player 1 Wins🥳. Better luck next time Player 2')
    elif space[2] and space[5] and space[8] == 'O':
        print('Player 2 Wins🥳. Better luck next time Player 1')
    else:
        player_input('player1', 'player2')

check_win()



# Function 4 Ex 4
# def play():
#     start = input('Write "Play" to Start')
#     if start == "Play":
#         print(display_board())
# play()

    
        