from tkinter import *
import tkinter as tk
import Checkers_Controller
import time

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', textvariable=None):
        super().__init__(master, textvariable=textvariable)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class Checkers_UI(Tk):
    WINDOW_SIZE = 600
    WINDOW_COLOR = 'beige'
    CELL_SIZE = (WINDOW_SIZE - WINDOW_SIZE / 5)/8
    WINDOW_SIZE = 600  # pixels
    GRID_LINE_WIDTH = 2  # pixels
    SYMBOL_WIDTH = WINDOW_SIZE / 24  # pixels - adjust ratio
    WHITE_BOARD_COLOR = "#eeddd2"
    DARK_BOARD_COLOR = "#c69b7c"
    BOARD_PLAYER1_SHAPE = 1
    BOARD_PLAYER2_SHAPE = 2
    BOARD_TILE_ROWS = 3

    TILE_ROWS = 3
    SYMBOL_SIZE = int(CELL_SIZE / 3)
    DARK_PLAYER_COLOR = 'white'
    WHITE_PLAYER_COLOR = 'tomato'
    DRAW_SCREEN_COLOR = 'light sea green'
    GRID_COLOR = 'light grey'
    BG_COLOR = 'white'
    FIRST_PLAYER = 2  # 1 - X, 2 = O
    STATE_TITLE_SCREEN = 0
    STATE_X_TURN = 1
    STATE_O_TURN = 2
    STATE_GAME_OVER = 3
    STATE_GAME_PLAYER2_TURN = 2
    STATE_GAME_PLAYER1_TURN = 1

    EMPTY = 0
    X = 1
    O = 2

    def __init__(self):
        Tk.__init__(self)

        self.init_start_window()


    def init_start_window(self):
        # placeholder title screen

        row = Frame(self, width = Checkers_UI.WINDOW_SIZE, height = Checkers_UI.WINDOW_SIZE)
        self.playerName = StringVar()
        self.gamePlayer = EntryWithPlaceholder(row, "Player 1", textvariable=self.playerName)
        self.gamePlayer.pack()

        startGameButton = Button(row, height=2, width=30, text="Start Game", command=self.init_start_game)
        startGameButton.pack()
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        self.row = row

    def init_start_game(self):
        self.clear()
        self.playerCounter = 0
        self.init_game_data()
        self.init_board_window()

    def init_game_data(self):
        self.gameController = Checkers_Controller.Checkers_Controller()
        self.gameController.init_players_data("")
        self.gameController.gameData.gameState = Checkers_UI.STATE_GAME_PLAYER2_TURN
        return

    def init_board_window(self):
        self.root = tk.Tk()

        self.canvasTop = tk.Canvas(self.root,
                                   height=Checkers_UI.WINDOW_SIZE / 5, width=Checkers_UI.WINDOW_SIZE,
                                   bg=Checkers_UI.WINDOW_COLOR
                                   )
        self.canvasBoard = tk.Canvas(self.root,
                                height=(Checkers_UI.WINDOW_SIZE - Checkers_UI.WINDOW_SIZE / 5),
                                width=(Checkers_UI.WINDOW_SIZE - Checkers_UI.WINDOW_SIZE / 5),
                                bg=Checkers_UI.WINDOW_COLOR)

        self.canvasTop.create_text(
            100,
            20,
            text='Player 1: ', fill='black',
            font=('Franklin Gothic', int(-Checkers_UI.WINDOW_SIZE / 36), 'bold'))

        self.draw_board()




        self.canvasBottom= tk.Canvas(self.root,
            height=Checkers_UI.WINDOW_SIZE / 5, width=Checkers_UI.WINDOW_SIZE,
            bg=Checkers_UI.WINDOW_COLOR)

        self.player2Label = tk.Label(self.root, text = "Player 2")
        self.player2Label.config(font=('Franklin Gothic', int(-Checkers_UI.WINDOW_SIZE / 36), 'bold'))
        self.canvasBottom.create_window(200, 100, window=self.player2Label)


        self.player2MoveLabel = tk.Label(self.root, text="Move")
        self.player2MoveLabel.config(font=('Franklin Gothic', int(-Checkers_UI.WINDOW_SIZE / 36), 'bold'))
        self.canvasBottom.create_window(300, 100, window=self.player2MoveLabel)

        self.playerMoveFrom = tk.StringVar(self.root)
        self.nextMoveFrom = Entry(self.canvasBottom, textvariable=self.playerMoveFrom)
        self.nextMoveFrom.pack()
        self.canvasBottom.create_window(400, 100, window = self.nextMoveFrom)

        self.playerMoveTo = tk.StringVar(self.root)
        self.nextMoveTo = Entry(self.canvasBottom, textvariable=self.playerMoveTo)
        self.nextMoveTo.pack()
        self.canvasBottom.create_window(450, 100, window=self.nextMoveTo)

        self.buttonMove = tk.Button(self.root, text='Move', command=self.do_move_click, bg='brown', fg='white',
                                    font=('helvetica', 9, 'bold'))
        self.canvasBottom.create_window(500, 100, window=self.buttonMove)

        self.canvasTop.pack()
        self.canvasBoard.pack()
        self.canvasBottom.pack()

    def do_move_click (self):
        if (self.gameController.gameData.gameState == Checkers_UI.STATE_GAME_PLAYER2_TURN):
            print ("str var")
            print (self.playerMoveFrom.get())
            print (self.playerMoveTo.get())


            if (self.gameController.newMove(self.playerMoveFrom.get(), self.playerMoveTo.get()) != None):
                self.draw_board()
                self.gameController.gameData.gameState = Checkers_UI.STATE_GAME_PLAYER1_TURN
        if (self.gameController.gameData.gameState == Checkers_UI.STATE_GAME_PLAYER1_TURN):
            self.gameController.newMoveVsComputer()
            self.canvasBoard.after(3, self.draw_board)
            self.gameController.gameData.gameState = Checkers_UI.STATE_GAME_PLAYER2_TURN
            print ("draw")

        return

    def draw_board(self):



        square = 0
        for y in range(0, self.gameController.gameData.board.boardSize):
            square = square + 1
            for x in range(0, self.gameController.gameData.board.boardSize):

                if square % 2 == 0:
                    self.canvasBoard.create_rectangle(Checkers_UI.CELL_SIZE * x, Checkers_UI.CELL_SIZE * y,
                                                      (Checkers_UI.CELL_SIZE * x + Checkers_UI.CELL_SIZE),
                                                      (Checkers_UI.CELL_SIZE * y + Checkers_UI.CELL_SIZE),
                                                      outline=Checkers_UI.WHITE_BOARD_COLOR,
                                                      fill=Checkers_UI.WHITE_BOARD_COLOR)
                else:
                    self.canvasBoard.create_rectangle(Checkers_UI.CELL_SIZE * x, Checkers_UI.CELL_SIZE * y,
                                                      (Checkers_UI.CELL_SIZE * x + Checkers_UI.CELL_SIZE),
                                                      (Checkers_UI.CELL_SIZE * y + Checkers_UI.CELL_SIZE),
                                                      outline=Checkers_UI.DARK_BOARD_COLOR,
                                                      fill=Checkers_UI.DARK_BOARD_COLOR)

                    if self.gameController.gameData.board.squares[y][x] == Checkers_UI.BOARD_PLAYER1_SHAPE:
                        self.canvasBoard.create_oval(Checkers_UI.CELL_SIZE * x + Checkers_UI.SYMBOL_SIZE,
                                                     Checkers_UI.CELL_SIZE * y + Checkers_UI.SYMBOL_SIZE,
                                                     (
                                                                 Checkers_UI.CELL_SIZE * x + Checkers_UI.CELL_SIZE - Checkers_UI.SYMBOL_SIZE),
                                                     (
                                                                 Checkers_UI.CELL_SIZE * y + Checkers_UI.CELL_SIZE - Checkers_UI.SYMBOL_SIZE),
                                                     width=Checkers_UI.SYMBOL_WIDTH,
                                                     outline=Checkers_UI.DARK_PLAYER_COLOR)
                    if self.gameController.gameData.board.squares[y][x] == Checkers_UI.BOARD_PLAYER2_SHAPE:
                        self.canvasBoard.create_oval(Checkers_UI.CELL_SIZE * x + Checkers_UI.SYMBOL_SIZE,
                                                     Checkers_UI.CELL_SIZE * y + Checkers_UI.SYMBOL_SIZE,
                                                     (
                                                                 Checkers_UI.CELL_SIZE * x + Checkers_UI.CELL_SIZE - Checkers_UI.SYMBOL_SIZE),
                                                     (
                                                                 Checkers_UI.CELL_SIZE * y + Checkers_UI.CELL_SIZE - Checkers_UI.SYMBOL_SIZE),
                                                     width=Checkers_UI.SYMBOL_WIDTH,
                                                     outline=Checkers_UI.WHITE_PLAYER_COLOR)

                square = square + 1
        self.canvasBoard.pack()
        return self.canvasBoard

    def gtpix(self, grid_coord):
        # gtpix = grid_to_pixels
        # for a grid coordinate, returns the pixel coordinate of the center
        # of the corresponding cell

        pixel_coord = grid_coord * Checkers_UI.CELL_SIZE + Checkers_UI.CELL_SIZE / 2
        return pixel_coord








    def exit(self, event):
        self.destroy()

    def clear(self):
        self.row.destroy()



def main():
    root = Checkers_UI()
    root.mainloop()

main()