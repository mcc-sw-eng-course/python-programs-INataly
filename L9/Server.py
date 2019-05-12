# Python program to implement server side of chat room.
import socket
import select
import sys
import threading
import ast
import Tic_Tac_Toe

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print
    "Correct usage: script, IP address, port number"
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind((IP_address, Port))

""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100)

list_of_clients = []

gameData = Tic_Tac_Toe.Game()

def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!")
    response_dict = dict()
    while True:
        try:
            data = conn.recv(2048)

            # Bucle de escucha. En él indicamos la forma de actuar al recibir las tramas del cliente
            input_dict = ast.literal_eval(data)
            if (type(input_dict) == "dict"):
                player = Tic_Tac_Toe.Player()
                message = input_dict["message"]
                if message == "init_player_data":
                    if gameData.player1 == None:
                        player.playerName = input_dict["player_name"]
                        player.playerShape = "X"
                        gameData.player1 = player
                    elif gameData.player2 == None:
                        player.playerName = input_dict["player_name"]
                        player.playerShape = "O"
                        gameData.player2 = player

                elif message == "new_move":
                    coord = input_dict["coord"]
                    nx = coord["x"]
                    ny = coord["y"]
                    playerShape = input_dict["player_shape"]
                    if playerShape == "X":
                        if (gameData.board.squares[nx][ny] == 0):
                            gameData.board.squares[nx][ny] = 1
                            playerMove = gameData.player1.newPlayerMove(coord)
                            gameData.turns.append(playerMove)
                            won_player = gameData.check_game_over()
                    elif playerShape == "O":
                        if (gameData.board.squares[nx][ny] == 0):
                            gameData.board.squares[nx][ny] = 2
                            playerMove = gameData.player1.newPlayerMove(coord)
                            gameData.turns.append(playerMove)
                            won_player = gameData.check_game_over()

                message_to_send = str(response_dict)
                broadcast(message_to_send, conn)

            else:
                """message may have no content if the connection 
                is broken, in this case we remove the connection"""
                remove(conn)

        except:
            continue


"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    """Accepts a connection request and stores two parameters,  
    conn which is a socket object for that user, and addr  
    which contains the IP address of the client that just  
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print
    addr[0] + " connected"

    # creates and individual thread for every user
    # that connects
    threading.settrace (clientthread, (conn, addr))

conn.close()
server.close()