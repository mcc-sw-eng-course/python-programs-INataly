import Tic_Tac_Toe
import ast
import Cliente

class Tic_Tac_Toe_Network_Opponent:
    STATE_GAME_OVER = 2
    STATE_GAME_IN_COURSE = 1
    STATE_GAME_NO_STARTED = 0
    def __init__(self):
        self.gameConnection = Cliente.Tic_tac_Toe_Client()
        self.player1Name = ""
        self.player2Name = ""
        self.player1shape = ""
        self.player2shape = ""

    def init_player_data(self, playerstr:str):
        parameters = dict()
        playerName = playerstr
        message = "init_player_data"
        parameters["message"] = message
        parameters["player_name"] = playerName
        response = self.gameConnection.sendMessage(str(parameters))
        player_dict = ast.literal_eval(response)
        self.player1Name = player_dict["player_name"]
        return player_dict

    def getPlayer1(self):
        return (self.player1Name)

    def getPlayer2(self):
        return (self.player1Name)

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

        coord = {"x": nx, "y": ny}

        parameters = dict()
        playerName = self.player1Name
        playerShape = self.player1shape

        message = "new_move"
        parameters["message"] = message
        parameters["player_name"] = playerName
        parameters["player_shape"] = playerShape
        parameters["coord"] = coord
        response = self.gameConnection.sendMessage(str(parameters))
        move_dict = ast.literal_eval(response)
        self.player1Name = move_dict["player_name"]
        return move_dict


