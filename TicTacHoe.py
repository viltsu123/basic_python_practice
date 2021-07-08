#The tic tac toe game begins
print('\n'*10)
print("Welcome to Tic Tac Hoe!")
print()
    #player symbol selection
player1 = input("please choose X or O for Player 1:")
player2 = ""
if player1 == "X":
    player2 = "O"
else:
    player2 = "X"
print("Thank you\nPlayer 2 is now {}".format(player2))
print("")

#player symbol selection end

#print board,takes a list of characters
def myboard(ls):
    max = len(' {ls[0]} | {ls[1]} | {ls[2]}') - 17#to take out the chars in {}
    print(f' {ls[0]} | {ls[1]} | {ls[2]}')
    print('-'*max)
    print(f' {ls[3]} | {ls[4]} | {ls[5]} ')
    print('-'*max)
    print(f' {ls[6]} | {ls[7]} | {ls[8]} ')

#print board end region

#start the game and give player1 the turn
playermoves = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
gameActive = True
playerturn = ""

def gamewinner():
    token = True
    if(playermoves[0] == playermoves[3] == playermoves[6] or
        playermoves[1] == playermoves[4] == playermoves[7] or
        playermoves[2] == playermoves[5] == playermoves[8] or
        playermoves[0] == playermoves[1] == playermoves[2] or
        playermoves[3] == playermoves[4] == playermoves[5] or
        playermoves[6] == playermoves[7] == playermoves[8] or
        playermoves[0] == playermoves[4] == playermoves[8] or
        playermoves[2] == playermoves[4] == playermoves[6]):
        print("")
        winner = ""
        if(player1 == playermoves[0]):
            winner = "Player 1"
            print("Holy SHIT, GAME OVER WE HAVE A WINNER " + winner + " CONGRATULATIONS!!!")
            token = False
        else:
            winner = "Player 2"
            print("Holy SHIT, GAME OVER WE HAVE A WINNER " + winner + " CONGRATULATIONS!!!")
            token = False

    return token



while gameActive:
    playerturn = "player1"
    myboard(playermoves)
    playermoves[int(input("Player 1, please make a move:"))] = player1
    myboard(playermoves)
    playermoves[int(input("Player 2, please make a move:"))] = player2
    myboard(playermoves)
    playermoves[int(input("Player 1, please make a move:"))] = player1
    myboard(playermoves)
    playermoves[int(input("Player 2, please make a move:"))] = player2
    myboard(playermoves)
    playermoves[int(input("Player 1, please make a move:"))] = player1
    myboard(playermoves)
    gameActive = gamewinner()
    playermoves[int(input("Player 2, please make a move:"))] = player2
    myboard(playermoves)
    gameActive = gamewinner()
    playermoves[int(input("Player 1, please make a move:"))] = player1
    myboard(playermoves)
    gameActive = gamewinner()
    playermoves[int(input("Player 2, please make a move:"))] = player2
    myboard(playermoves)
    gameActive = gamewinner()
