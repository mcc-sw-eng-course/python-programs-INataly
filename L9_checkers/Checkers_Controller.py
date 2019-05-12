import math
import checkers

class Checkers_Controller:
    STATE_GAME_OVER = 2
    STATE_GAME_IN_COURSE = 1
    STATE_GAME_NO_STARTED = 0
    def __init__(self):
        self.gameData = checkers.Game()

    def  init_players_data(self, player1str:str, player2str:str = ""):
        player1 = checkers.Player()
        player2 = checkers.Player()
        player1.playerName = player1str
        if (player2str == ""):
            player2.playerName = "Computer"
            player2.isPc = True

        else:
            player2.playerName = player2str

        player1.playerShape = "X"
        player2.playerShape = "O"
        self.gameData.player1 = player1
        self.gameData.player2 = player2
        print (player1)

    def getPlayer1(self):
        return (self.gameData.player1.playerName)

    def getPlayer2(self):
        return (self.gameData.player2.playerName)

    def newMove(self, fromCoord, moveCoord):


        if (len(fromCoord) == 2 and len(moveCoord) == 2 and
            self.gameData.board.coordinatesLet.index(fromCoord[0]) >= 0 and
            self.gameData.board.coordinatesNum.index(fromCoord[1]) >= 0 and
            self.gameData.board.coordinatesLet.index(moveCoord[0]) >= 0 and
            self.gameData.board.coordinatesNum.index(moveCoord[1]) >= 0):

            fromCoord = self.gameData.board.coordinatesDict[fromCoord]
            fromCoordX = fromCoord["x"]
            fromCoordY = fromCoord["y"]
            moveCoord = self.gameData.board.coordinatesDict[moveCoord]
            moveCoordX = moveCoord["x"]
            moveCoordY = moveCoord["y"]

            if self.gameData.board.squares[fromCoordY][fromCoordX] == checkers.Board.BOARD_PLAYER2_SHAPE:
                if (abs(fromCoordX - moveCoordX) == 1 and fromCoordY < 8 and moveCoordX >= 0 and fromCoordY - moveCoordY == 1
                    and self.gameData.board.squares[moveCoordY][moveCoordX] == checkers.Board.BOARD_EMPTY_SHAPE):

                    self.gameData.board.squares[fromCoordY][fromCoordX] = checkers.Board.BOARD_EMPTY_SHAPE
                    self.gameData.board.squares[moveCoordY][moveCoordX] = checkers.Board.BOARD_PLAYER2_SHAPE
                    playerMove = self.gameData.player2.newPlayerMove(fromCoord, moveCoord)
                    self.gameData.turns.append(playerMove)
                    self.gameData.check_game_over()
                    return playerMove

                if (fromCoordX - moveCoordX == 2 and fromCoordX < 8 and moveCoordX >= 0 and fromCoordY - moveCoordY == 2 and fromCoordY < 8 and moveCoordY >= 0
                    and self.gameData.board.squares[fromCoordY - 1][fromCoordX - 1] == checkers.Board.BOARD_PLAYER1_SHAPE
                    and self.gameData.board.squares[moveCoordY][moveCoordX] == checkers.Board.BOARD_EMPTY_SHAPE):

                    self.gameData.board.squares[fromCoordY][fromCoordX] = checkers.Board.BOARD_EMPTY_SHAPE
                    self.gameData.board.squares[fromCoordY - 1][fromCoordX - 1] = checkers.Board.BOARD_EMPTY_SHAPE
                    self.gameData.board.squares[moveCoordY][moveCoordX] = checkers.Board.BOARD_PLAYER2_SHAPE
                    playerMove = self.gameData.player2.newPlayerMove(fromCoord, moveCoord)
                    self.gameData.turns.append(playerMove)
                    self.gameData.check_game_over()
                    return playerMove

                if (fromCoordX - moveCoordX == -2 and fromCoordX < 8 and moveCoordX >= 0 and fromCoordY - moveCoordY == 2 and fromCoordY < 8 and moveCoordY >= 0
                    and self.gameData.board.squares[fromCoordY - 1][fromCoordX + 1] == checkers.Board.BOARD_PLAYER1_SHAPE
                    and self.gameData.board.squares[moveCoordY][moveCoordX] == checkers.Board.BOARD_EMPTY_SHAPE):

                    self.gameData.board.squares[fromCoordY][fromCoordX] = checkers.Board.BOARD_EMPTY_SHAPE
                    self.gameData.board.squares[fromCoordY - 1][fromCoordX + 1] = checkers.Board.BOARD_EMPTY_SHAPE
                    self.gameData.board.squares[moveCoordY][moveCoordX] = checkers.Board.BOARD_PLAYER2_SHAPE
                    playerMove = self.gameData.player2.newPlayerMove(fromCoord, moveCoord)
                    self.gameData.turns.append(playerMove)
                    self.gameData.check_game_over()
                    return playerMove


        return None

    def newMoveVsComputer(self):
        resultMove = self.gameData.player2.newComputerGeneratedRandomMove(self.gameData.board)
        if resultMove != None:
            fromCoord = resultMove.fromPlace
            fromCoordX = fromCoord["x"]
            fromCoordY = fromCoord["y"]
            self.gameData.board.squares[fromCoordY][fromCoordX] = checkers.Board.BOARD_EMPTY_SHAPE

            moveCoord = resultMove.movePlace
            moveCoordX = moveCoord["x"]
            moveCoordY = moveCoord["y"]
            self.gameData.board.squares[moveCoordY][moveCoordX] = checkers.Board.BOARD_PLAYER1_SHAPE

            if resultMove.enemyPlace != None:
                enemyCoord = resultMove.enemyPlace
                enemyCoordX = enemyCoord["x"]
                enemyCoordY = enemyCoord["y"]
                self.gameData.board.squares[enemyCoordY][enemyCoordX] = checkers.Board.BOARD_EMPTY_SHAPE
            print ("------------------------")
            for y in range(0, 8):
                line = ""
                for x in range(0, 8):
                    line = line + " " + str(self.gameData.board.squares[y][x])

                print (line)

            return resultMove
        return None

