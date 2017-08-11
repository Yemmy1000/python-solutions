print("-----> Author          : Amujo Oluyemi E")
print("-----> Matric No       : 16483005")
print("-----> Course of Study : Comp Sc - Information Security")
print("-----> Email           : oluyemiamujo@gmail.com")
print("-----> Phone No        : 07063717176")
print("-----> Program Title   : TIC-TAC-TOE")

from random import randrange


current_board = [1,2,3,4,5,6,7,8,9]
play_symbol = ''
def resetboard():
    board = [1,2,3,4,5,6,7,8,9]
    return board

def No_of_player():
    playerNo = eval(input("\n Enter No of player - 1 or 2: "))
    if playerNo == 1:
        play_mode, player0, player1 = 'Human vs Machine',  0, 1
        return play_mode, player0, player1

    else:
        play_mode, player0, player1 = 'Human vs Human', 0, 1
        return play_mode, player0, player1
        
def play(player, bd):   #prints the player number (0 or 1) and prompts the player  to enter a box value that have not changed to 'O' or 'X'

    box_value = int(input("Player 0 Enter a box value: "))   
    halt = False
    while not halt :
        if (bd[box_value-1] == 'O' ) :
            print("Player", player, " retry box value! ")

        else :
            valid_value = box_value
            halt = True
            

    current_board = changeBoard(valid_value, player)
    return current_board

def machinePlay(player, bd):    #plays the role of the player using random number. This function generates numbers in the interval [1,9] and uses the first generated random number that has not been used to play the game.
    print("Player 1 is playing, be patient! ")
    
   # sleep(1)
    halt = False
    
    while not halt :
        #box_value = 0
        box_value = randrange(1,9)
        if (bd[box_value-1] == 'O') :
            print("Player", player, " retry box value! ")
        elif (bd[box_value-1] == 'X') :
            print("Player", player, " retry box value! ")
        else:
            halt = True

    cur_board = changeBoard(box_value, player)
    
    return cur_board
    

def changeBoard(box_value, player): #using the chosen box number to change the value of the box to O or X depending on whether the player is 0 or 1, respectively.
    if player == 0 :
        play_symbol = 'O'
    elif player == 1 :
        play_symbol = 'X'

    for item in range(len(current_board)) :
        if current_board[item] == box_value :
            current_board[item] = play_symbol
            
    return current_board


def printBoard(board):
    print("\n The current TicTacToe Board... ")
    print('|', board[0], '|', board[1], '|', board[2], '|',)
    print('|', board[3], '|', board[4], '|', board[5], '|',)
    print('|', board[6], '|', board[7], '|', board[8], '|',)


def checkRows(board) :  #checks to see which of the rows of the board has the same value and returns True, otherwise, returns False
    board_row = False
    if board[3] == board[4] == board[5] :
        board_row = True
    return board_row

    
def checkCols(board) :  #checks to see which of the cols of the board has the same value and returns True, otherwise, returns False
    board_col = False
    if board[1] == board[4] == board[7] :
        board_col = True
    return board_col

def checkDiagonal1(board) :  # checks to see which of the diagonals of the board has the same value and returns True, otherwise, returns False
    board_diag1 = False
    if board[0] == board[4] == board[8] :
        board_diag1 = True
    return board_diag1

def checkDiagonal2(board) :  # checks to see which of the diagonals of the board has the same value and returns True, otherwise, returns False
    board_diag2 = False
    if board[2] == board[4] == board[6] :
        board_diag2 = True
    return board_diag2


def win(player) :   #checks if a player wins the game, returns True of the player wins  and False otherwise
    board_row = False
    if board[3] == board[4] == board[5] :
        board_row = True
    return board_row


def main():
    current_board = resetboard()
    play_mode, player0, player1 = No_of_player()
    print("The Play Mode is ", play_mode, " Player1 is ", player0, " while Player2 is ", player1, " !" )
    printBoard(current_board)

    quit = False

    while not quit:
        select_player = player0
        cur_board = play(select_player, current_board)
        printBoard(cur_board)
        if ( checkRows(cur_board) or checkCols(cur_board) or checkDiagonal1(cur_board) or checkDiagonal2(cur_board) ):
            print("Player0 wins! Game quit!!!")
            quit = True
            
        else:  
            select_player = player1
            machinePlay(select_player, current_board)
            printBoard(cur_board)
            if ( checkRows(cur_board) or checkCols(cur_board) or checkDiagonal1(cur_board) or checkDiagonal2(cur_board) ):
                print("Player1 wins! Game quit!!!")
                quit = True
        

main()
    
