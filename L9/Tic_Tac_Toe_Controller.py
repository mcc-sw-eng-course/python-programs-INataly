import Tic_Tac_Toe

class Tic_Tac_Toe_Controller:
    STATE_GAME_OVER = 2
    STATE_GAME_IN_COURSE = 1
    STATE_GAME_NO_STARTED = 0
    def __init__(self):
        self.gameData = Tic_Tac_Toe.Game()

    def  init_players_data(self, player1str:str, player2str:str = ""):
        player1 = Tic_Tac_Toe.Player()
        player2 = Tic_Tac_Toe.Player()
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

    def newMove(self, x, y, cell_size):
        ny = 0
        nx = 0
        for yi in range(1, 4):
            if y <= cell_size * yi:
                ny = yi - 1
                for xi in range(1, 4):
                    if x <= cell_size * xi:
                        nx = xi - 1
                        break
                break

        if (self.gameData.board.squares[nx][ny] == 0):
            self.gameData.board.squares[nx][ny] = 1
            coord = {"x": nx, "y": ny}
            playerMove = self.gameData.player1.newPlayerMove(coord)
            self.gameData.turns.append(playerMove)
            self.gameData.check_game_over()
            return playerMove


        return None

    def newMoveVsComputer(self,cell_size):
        resultMove = self.gameData.player2.newComputerGeneratedRandomMove(self.gameData.board.squares)
        if resultMove != None:
            self.gameData.turns.append(resultMove)
            self.gameData.board.squares[resultMove.movePlace["x"]][resultMove.movePlace["y"]] = 2
            grid_place =  resultMove.movePlace
            grid_place["x"] = (resultMove.movePlace["x"] + 1)* cell_size * .99
            grid_place["y"] = (resultMove.movePlace["y"] + 1) * cell_size * .99
            game_result = self.gameData.check_game_over()
            return grid_place
        return None

