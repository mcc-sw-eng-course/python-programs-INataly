import math
from random import *

class Move:
    def __init__(self):
        self.player = None
        self.movePlace = {"x": -1, "y": -1}

class Player:
    def __init__(self):
        self.playerName = ""
        self.playerShape = ""
        self.isPc = False

    def newComputerGeneratedRandomMove(self, board):
        randomList = list()
        for x in range(0, 3):
            for y in range (0, 3):
                if board[x][y] == 0:
                    newXY = {"x" : x, "y" : y}
                    randomList.append(newXY)

        if (len(randomList) >= 1):
            nXY = 0
            if len(randomList) > 1:
                randomNum = len(randomList) - 1
                nXY = randint(0, randomNum)

            newMove = Move()
            newMove.movePlace = randomList[nXY]
            newMove.player = self
            return newMove
        return None


    def newPlayerMove(self, coord):
        newMove = Move()
        newMove.movePlace = coord
        newMove.player = self
        return newMove



class Board:
    def __init__(self):
        self.squares = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

class Game:
    STATE_GAME_NO_STARTED = 0
    STATE_GAME_PLAYER1_TURN = 1
    STATE_GAME_PLAYER2_TURN = 2
    STATE_GAME_IN_COURSE = 3
    STATE_GAME_OVER = 4


    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.board = Board()
        self.turns = list()
        self.gameState = Game.STATE_GAME_NO_STARTED
        self.winner_player = None

    def get_player_start(self):
        x = randint(1, 100)
        return (x % 2)

    def check_game_over(self):

        game_won = 0
        Xd1 = 0
        Od1 = 0
        Xd2 = 0
        Od2 = 0
        Os = 0
        for x in range(0, 3):
            Xy = 0
            Oy = 0
            Xx = 0
            Ox = 0

            for y in range (0, 3):

                if self.board.squares[x][y] == 1:
                    Xy = Xy + 1

                if self.board.squares[x][y] == 2:
                    Oy = Oy + 1

                if self.board.squares[y][x] == 1:
                    Xx = Xx + 1

                if self.board.squares[y][x] == 2:
                    Ox = Ox + 1

                if x == y and self.board.squares[y][x] == 1:
                    Xd1 = Xd1 + 1

                if x == y and self.board.squares[y][x] == 2:
                    Od1 = Od1 + 1

                if ((x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)):
                    if self.board.squares[y][x] == 1:
                        Xd2 = Xd2 + 1

                    if self.board.squares[y][x] == 2:
                        Od2 = Od2 + 1

                if self.board.squares[y][x] == 0:
                    Os = Os + 1

                if (Xy == 3 or Xx == 3):
                    game_won = 1
                    self.winner_player = self.player1
                    self.gameState = Game.STATE_GAME_OVER
                    break
                if (Oy == 3 or Ox ==3):
                    game_won = 2
                    self.gameState = Game.STATE_GAME_OVER
                    self.winner_player = self.player2
                    break

            if (Xd1 == 3 or Xd2 == 3):
                game_won = 1
                self.gameState = Game.STATE_GAME_OVER
                self.winner_player = self.player1

            if (Od1 == 3 or Od2 == 3):
                game_won = 2
                self.gameState = Game.STATE_GAME_OVER
                self.winner_player = self.player2

            if (self.gameState == Game.STATE_GAME_OVER):
                break

        if (Os == 0):
            self.gameState = Game.STATE_GAME_OVER

        return  game_won

