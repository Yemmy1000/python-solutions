#Begin Program

#import random number generator from random library
from random import randint, seed


#Global variable board representing the ticTacToe board
board = [1,2,3,4,5,6,7,8,9]


#This module resets the ticTacToe board to the original values
def reset():
    for k in range(1,10):   #loop through a sequence [1,2,3,..,9]
        board[k-1] = k

#This module prints the ticTacToe board in a 3 by 3 matrix
#using the format
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
def printBoard():
    print('\nThe current TicTapToe Board')
    for m in range(3): 
        string = '| '
        for n in range(3):
            if board[n+3*m] == 0:
                string = string + ' O |'
            elif board[n+3*m] == -1:
                string = string + ' X |'
            else:
                string = string + ' ' + str(board[n+3*m]) + ' |'
        print(string)

#This module changes the value (num1) of a box in the ticTacTop board chosen
# by player 0 to 0 and player 1 to -1
#
def changeBoard(num1,player):
    for k in range(len(board)):
        if board[k] == num1 and player == 0:
            board[k] = 0
        elif board[k] == num1 and player == 1:
            board[k] = -1
#This module prompts the player to enter a box value. The format is
# 'Player <player number> Enter a box value'
#
def play(player):
    print('Player', player, end=' ')
    sValue = int(input('Enter a box value: '))
    changeBoard(sValue, player)
    printBoard()

#This module checks if boxes in anyone of the rows have the same value
#The module returns True if that is the case and False otherwise
#
def checkRows(value):
    #Complete
    if board[0] == value and board[1] == value and board[2] == value:
        return True
    elif board[3] == value and board[4] == value and board[5] == value:
        return True
    elif board[6] == value and board[7] == value and board[8] == value:
        return True
    else:
        return False
#
#This module checks if boxes in anyone of the cols have the same value
#The module returns True if that is the case and False otherwise
#
def checkCols(value):
     #Complete
    if board[0] == value and board[3] == value and board[6] == value:
        return True
    elif board[1] == value and board[4] == value and board[7] == value:
        return True
    elif board[2] == value and board[5] == value and board[8] == value:
        return True
    else:
        return False
#
#This module checks if boxes in anyone of the diagonals have the same value
#The module returns True if that is the case and False otherwise
#
def checkDiagonal(value):
    #Complete
    if board[0] == value and board[4] == value and board[8] == value:
        return True
    elif board[6] == value and board[4] == value and board[2] == value:
        return True
    else:
        return False
     

#This module determines whether or not a player wins after playing the
#  a turn. This module uses checkDiagonal, checkRows and checkCols to
#  ascertain if the player wins. As least one of the options (checkDiagonal,
#  checkCols and checkRows must return a True.
#  This module returns True if the player wins and False, otherwise
#  This module also print
#  'Player 0 Wins'  if player 0 wins
#  'Player 1 Wins' if player 1 wins

def win(player):
    #Complete
    if player == 0:
        value = 0
        if checkRows(value) == True or checkCols(value) == True or checkDiagonal(value) == True:
            print("*********************")
            print("*** Player 0 Wins ***")
            print("*********************")
            return True
        else:
            return False

    else:
        value = -1
        if checkRows(value) == True or checkCols(value) == True or checkDiagonal(value) == True:
            print("*********************")
            print("*** Player 1 Wins ***")
            print("*********************")
            return True
        else:
            return False

#This module is only for 1 player only. In this case, this player
#plays with the machine. The machine uses random numbers. Random numbers are
#generated and tested to determine whether or not the generated random number has been
#played. The first generated random number that has not been played is chosen.
#If after 100 trials, no unplayed is found, nothing is done and a warning is
#sent to the player. IT IS ASSUMED THAT THIS SCENARIO WILL NOT OCCUR. NOTE THAT
#THERE IS NOT INTELLIGENCE BUILT IN TO PROGRAM THAT WILL ALLOW COMPUTER TO
#CHOOSE THE BEST NUMBER TO PLAY. YOU WILL RECEIVE BONUS POINT IF YOU COULD
#MODIFY THE MODULE TO ALLOW COMPUTER SELECT THE BEST NUMBER.
#

def machinePlay(player):
    print('Player ', player, '***Computer*** playing')
    seed()
    r = randint(1,9)
    index = 0
    while index<100 and (board[r-1] ==0 or board[r-1] ==-1):
        r = randint(1,9)
        index = index + 1
    if index < 100:
        changeBoard(r,player)
        printBoard()
    else:
        print('Computer could not play after 100 trials')
    
#The module plays the tictactoe game, using modules defined above.
#The module allows players to play any number of games until the
# payer(s) decides to quit. This represent the first while loop.
#The second while loop allows players to take turns making rounds. Note that
#since there are 9 box numbers total, the maximum number of rounds is 9. If
# after 9 rounds and there is no winner, the board is reset and player(s) will
# prompted to determine whether or not to start a new game.
#
def ticTacToe(numPlayers):
    quitPlay = 'n'
    while  (quitPlay == 'n'): #interested in continuing with a new game
        reset()               #reset board to the original fomr
        printBoard()          #Display the current state of the board
        if numPlayers == 2:   #Number of players is 2
            playover = False  #play not over
            rounds = 0        # initial round
            while not(playover) and rounds<9:  #play until it is won
                                               # or rounds exhausted
                player = 0    #first player's turn
                play(player)
                playover = win(player)
                rounds = rounds + 1
                if not(playover) and rounds <9 : #second player's turn
                                                 #only when first player
                                                 #did not win
                    player = 1
                    play(player)
                    playover = win(player)
                    rounds = rounds + 1
            if rounds >= 9:         #rounds is exhausted; it is a draw
                print("It is a draw")
        elif numPlayers == 1:    #one player only, playing with the computer
            playover = False  #play is not over
            rounds = 1        #initial round
            while not(playover) and rounds<=9:  #play until it is won
                player = 0     #first player's turn
                play(player)
                playover = win(player)
                rounds = rounds + 1
                if not(playover) and rounds <9 : #second player's turn
                                                 #computer's turn to play
                    player = 1
                    machinePlay(player)
                    playover = win(player)
                    rounds = rounds + 1
            if rounds > 9:
                print("It is a draw")           

        else:
            print('Oohs! Number of players is not 1 or 2') #wrong number
                                                           #of players
            quitPlay = 'y'
        if quitPlay != 'y':
            quitPlay = input('Do you want to quit?')

def main():    #run the tictactoe program
    print('Welcome to TicTacToe Game')
    print('CSC 120 Project: Fayetteville State University, NC')
    print('This game can be played by one or two players')
    numPlayers = int(input('Enter the number of players, 1/2 for one/two players: '))
    ticTacToe(numPlayers)
    print('Thanks for playing TicTapToe!')

main()

#End Program



