#encoding=utf-8

from contextlib import nullcontext
import itertools
from json.encoder import INFINITY
import math


board = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*']
]



def checkIfWon(type):
    # 'type' is whether the checking factor is "O" or "X"
    counter=0
    for i in board:
        for i in range (0,3,1):
            if (board[i][0] == type and board[i][1] == type and board[i][2]==type):
                return True
                # horizontal
    for i in board:
        for i in range (0,3,1):
            if board[0][i] == type and board[1][i] == type and board[2][i]==type:
                return True
                # vertical
    if board[0][0]==type and board[1][1]==type and board[2][2]==type:
        return True
    elif board[0][2]==type and board[1][1]==type and board[2][0]==type:
        return True
    for i in board[0]:
        if i =="*":
            counter+=1
    for i in board[1]:
        if i =="*":
            counter+=1
    for i in board[2]:
        if i =="*":
            counter+=1
    if counter==0:
        return "Draw"
    else:
        return False


def gameStart(player, whosPlaying, ai):
    whoWon=-1
    if whosPlaying=="Player":
        print("\n ",*board[0][0],"",*board[0][1],"",*board[0][2],"\n ",*board[1][0],"",*board[1][1],"",*board[1][2],"\n ",*board[2][0],"",*board[2][1],"",*board[2][2],"\n ")
        playersTurn=True
    else:
        playersTurn=False
    playerMove=""
    while playersTurn==True:
        while True:
            try:
                playerMove = int(input("Enter an index of the field between 1 and 9: "))
                if 1 <= playerMove <= 9:
                    if 0<=playerMove<=3:
                        if board[0][playerMove-1]!="*":
                            raise ValueError() 
                    elif 3<=playerMove<=6:
                        if board[1][playerMove-4]!="*":
                            raise ValueError()
                    elif 6<=playerMove<=9:
                        if board[2][playerMove-7]!="*":
                            raise ValueError()
                    break
                raise ValueError()
            except ValueError:
                print("Error")
        if 0>=playerMove or playerMove<=3:
            board[0][playerMove-1]=player
        elif 3>playerMove or playerMove<7:
            board[1][playerMove-4]=player
        elif 6>playerMove or playerMove<10:
            board[2][playerMove-7]=player
        result=checkIfWon(player)
        if result==True:
            whoWon="Player"
        playersTurn=""
    if playersTurn==False:
            aiMove=bestMove(ai, player)
            board[aiMove[0]][aiMove[1]]=ai
            result=checkIfWon(ai)
            if result==True:
                whoWon="Computer"
            playersTurn=True
    if result==True:
        return True, whoWon 
    elif result=="Draw":
        return True, "Draw"
    else: 
        return False, ""


def game():
    print("\n\nWelcome to tic tac toe")
    player=""
    while player!="o" and player!="X" and player!="x" and player!="O":
        player=input("\nPlease type what you would like to be (O/X): ")
    if player =="o" or player=="O":
        player="O"
        ai="X"
        whosPlaying="Computer"
    elif player=="x" or player=="X":
        player="X"
        ai="O"
        whosPlaying="Player"
    ended=False
    while ended==False:
        ended,whoWon=gameStart(player, whosPlaying, ai)
        if whosPlaying == "Computer":
            whosPlaying="Player"
        else:
            whosPlaying="Computer"
    if whoWon!="Draw":
        print("\n ",*board[0][0],"",*board[0][1],"",*board[0][2],"\n ",*board[1][0],"",*board[1][1],"",*board[1][2],"\n ",*board[2][0],"",*board[2][1],"",*board[2][2],"\n ")
        if whoWon!="Computer":
            print("Coungratulations you won!\n" )
        else:
            print("The AI beat you!\n")
            answer=0
            while answer!="yes" and answer!="Yes" and answer!="no" and answer!="No":
                answer=input("Wanna go again?")
            if answer=="yes" or answer=="Yes":
                game()
    else:
        print("\n ",*board[0][0],"",*board[0][1],"",*board[0][2],"\n ",*board[1][0],"",*board[1][1],"",*board[1][2],"\n ",*board[2][0],"",*board[2][1],"",*board[2][2],"\n ")
        print("Draw")

# AI part of script

def bestMove(ai, player):
    if ai=="O":
        isO=True
    else:
        isO=False
    bestScore=-INFINITY
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j]=='*':
                board[i][j]=ai
                score = minimax(board, 0, False, ai, player, isO)
                board[i][j]='*'
                if score>bestScore:
                    bestScore=score
                    move=[i,j]
    return move

scores= {
    "X": 1,
    "O": -1,
    "Draw": 0
}

scores2= {
    "X": -1,
    "O": 1,
    "Draw": 0
}

def minimax(board, depth, isMaxzimizing, ai, player, isO):
    result = mcheckIfWon(ai, player)
    if result!=False:
        if isO:
            return scores2[result]
        else:
            return scores[result]
    if isMaxzimizing:
        bestScore=-INFINITY 
        for i in range (0,3):
            for j in range (0,3):
                if board[i][j]=='*':
                    board[i][j]=ai
                    score = minimax(board, depth+1, False, ai, player, isO)
                    board[i][j]='*'
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore=INFINITY
        for i in range (0,3):
            for j in range (0,3):
                if board[i][j]=='*':
                    board[i][j]=player
                    score = minimax(board, depth+1, True, ai, player, isO)
                    board[i][j]='*'
                    bestScore=min(score, bestScore)
        return bestScore

# Checks wheter the player has won or the AI has won or the third case, if it's a draw.
def mcheckIfWon(ai, player):
    result = checkIfWon(ai)
    result2 = checkIfWon(player)
    if result == True:
        return ai
    if result2 ==True:
        return player
    if result=="Draw" or result2=="Draw":
        return "Draw"
    else:
        return False
            

game()