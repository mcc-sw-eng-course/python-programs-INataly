import math
from random import *

class Move:
    def __init__(self):
        self.player = None
        self.movePlace = {"x": -1, "y": -1}
        self.fromPlace = {"x": -1, "y": -1}
        self.enemyPlace = {"x": -1, "y": -1}

class Player:
    def __init__(self):
        self.playerName = ""
        self.playerShape = ""
        self.isPc = False

    def newComputerGeneratedRandomMove(self, board):
        randomList = list()
        fromList = list()
        enemyList = list()
        for y in range(0, board.boardSize):
            for x in range(0, board.boardSize):
                if board.squares[y][x] == Board.BOARD_PLAYER1_SHAPE:
                    if (y + 1) < 8 and (x + 1) < 8 and board.squares[y + 1][x + 1] == Board.BOARD_EMPTY_SHAPE:
                        newXY = {"x": x + 1, "y": y + 1}
                        fromXY = {"x": x, "y": y}
                        randomList.append(newXY)
                        fromList.append(fromXY)
                        enemyList.append(None)
                    if (y + 1) < 8 and (x - 1) >= 0 and board.squares[y + 1][x - 1] == Board.BOARD_EMPTY_SHAPE:
                        newXY = {"x": x - 1, "y": y + 1}
                        fromXY = {"x": x, "y": y}
                        randomList.append(newXY)
                        fromList.append(fromXY)
                        enemyList.append(None)
                    if (y + 1) < 8 and (x + 1) < 8 and board.squares[y + 1][x + 1] == Board.BOARD_PLAYER2_SHAPE:
                        if (y + 2) < 8 and (x + 2) < 8 and board.squares[y + 2][x + 2] == Board.BOARD_EMPTY_SHAPE:
                            newXY = {"x": x + 2, "y": y + 2}
                            fromXY = {"x": x, "y": y}
                            enemyPlace =  {"x": x+1, "y": y+1}
                            randomList.append(newXY)
                            fromList.append(fromXY)
                            enemyList.append(enemyPlace)
                    if (y + 1) < 8 and (x - 1) >= 0 and board.squares[y + 1][x - 1] == Board.BOARD_PLAYER2_SHAPE:
                        if (y + 2) < 8 and (x - 2) >= 0 and board.squares[y + 2][x - 2] == Board.BOARD_EMPTY_SHAPE:
                            newXY = {"x": x - 2, "y": y + 2}
                            fromXY = {"x": x, "y": y}
                            enemyPlace =  {"x": x-1, "y": y+1}
                            randomList.append(newXY)
                            fromList.append(fromXY)
                            enemyList.append(enemyPlace)

        if (len(randomList) >= 1):
            nXY = 0
            if len(randomList) > 1:
                randomNum = len(randomList) - 1
                nXY = randint(0, randomNum)

            newMove = Move()
            newMove.movePlace = randomList[nXY]
            newMove.fromPlace = fromList[nXY]
            newMove.enemyPlace = enemyList[nXY]
            return newMove
        return None


    def newPlayerMove(self, fromCoord, moveCoord):


        newMove = Move()
        newMove.fromPlace = fromCoord
        newMove.movePlace = moveCoord
        newMove.player = self
        return newMove



class Board:
    BOARD_PLAYER1_SHAPE = 1
    BOARD_PLAYER2_SHAPE= 2
    BOARD_EMPTY_SHAPE = 0
    BOARD_TILE_ROWS = 3

    def __init__(self):
        self.boardSize = 8
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]
        square = 0
        self.coordinatesDict = dict()
        self.coordinatesLet = ["a","b","c","d","e","f","g","h"]
        self.coordinatesNum = ["8", "7", "6", "5", "4", "3", "2", "1"]

        for y in range(0, self.boardSize):
            square = square + 1
            for x in range(0, self.boardSize):
                if square % 2 == 1:
                    if y < Board.BOARD_TILE_ROWS:
                        self.squares [y][x] = Board.BOARD_PLAYER1_SHAPE
                    if y >= (8 - Board.BOARD_TILE_ROWS):
                        self.squares[y][x] = Board.BOARD_PLAYER2_SHAPE
                coordinate = self.coordinatesLet[x] + self.coordinatesNum[y]
                self.coordinatesDict[coordinate] = {"x": x, "y": y}
                square = square + 1
        print (self.coordinatesDict)

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
        Xy = 0
        Oy = 0

        for x in range(0, self.board.boardSize):


            for y in range (0,  self.board.boardSize):

                if self.board.squares[y][x] == Board.BOARD_PLAYER1_SHAPE:
                    Xy = Xy + 1

                if self.board.squares[y][x] == Board.BOARD_PLAYER2_SHAPE:
                    Oy = Oy + 1

        if (Xy == 0):
            game_won = 2
            self.gameState = Game.STATE_GAME_OVER
            self.winner_player = self.player2

        if (Oy == 0):
            game_won = 1
            self.gameState = Game.STATE_GAME_OVER
            self.winner_player = self.player1

        return  game_won

