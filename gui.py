# gui.py
import tkinter as tk
from config import BOARD_SIZE, TILE_COLORS, FONT_SETTINGS, CELL_WIDTH, CELL_HEIGHT
from game_logic import init_board, add_new_tile, move_left, move_right, move_up, move_down, can_move

class Game2048GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.board = init_board()
        self.history = []
        self.score = self.compute_score(self.board)
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Helvetica", 20), bg="azure3")
        self.score_label.pack(pady=10)
        self.board_frame = tk.Frame(self.master, bg="azure3")
        self.board_frame.pack(pady=10)
        self.grid_cells = []
        self.over_frame = None
        self.setup_GUI()
        self.update_GUI()
        # Enlaza las teclas de dirección para mover el juego.
        self.master.bind("<Key>", self.key_handler)

    def setup_GUI(self):
        """Configura la ventana y crea la cuadrícula de celdas."""
        background = tk.Frame(self.board_frame, bg='azure3', bd=3, relief="sunken")
        background.grid(row =0, column=0, padx=10, pady=10)
        score_frame = tk.Frame(self.master)
        score_frame.pack(pady=5)
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                # Configura cada celda usando los parámetros definidos en config.py.
                cell = tk.Label(background, text="", width=CELL_WIDTH, height=CELL_HEIGHT,
                                font=FONT_SETTINGS,
                                bg=TILE_COLORS.get(0, "azure4"), fg="white",
                                relief="raised", borderwidth=2)
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.grid_cells.append(row)

    def update_GUI(self):
        """Actualiza la visualización de cada celda en función del estado actual del tablero."""
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = self.board[i][j]
                # Selecciona el color de fondo según el valor; si no se encuentra, se usa 'orange'.
                color = TILE_COLORS.get(value, "orange") if value != 0 else TILE_COLORS.get(0, "azure4")
                text = str(value) if value != 0 else ""
                self.grid_cells[i][j].configure(text=text, bg=color)
        self.score = self.compute_score(self.board)
        self.score_label.configure(text=f"Score: {self.score}")
        self.master.update_idletasks()

    def key_handler(self, event):
        """Maneja las pulsaciones de teclado y actualiza el juego según la tecla presionada."""
        key = event.keysym
        
        if key.lower() == "u":
            if self.history:
                self.board = self.history.pop()
                if self.over_frame is not None:
                    self.over_frame.destroy()
                    self.over_frame = None
                self.update_GUI()
            return
        
        # Al realizar un movimiento, guarda el estado actual del tablero en el historial.
        previous_board = [row[:] for row in self.board]
        
        if key == "Up":
            new_board = move_up(self.board)
        elif key == "Down":
            new_board = move_down(self.board)
        elif key == "Left":
            new_board = move_left(self.board)
        elif key == "Right":
            new_board = move_right(self.board)
        else:
            return
        
        # Solo se guarda el historial si el tablero ha cambiado.
        if new_board != self.board:
            self.history.append(previous_board)
            self.board = new_board
            add_new_tile(self.board)
            self.update_GUI()
            if not can_move(self.board):
                self.game_over()

    def game_over(self):
        """Muestra un mensaje de 'Game Over' en pantalla."""
        # Si ya existe un mensaje de game over, no hace nada.
        if self.over_frame is not None:
            return
        self.over_frame = tk.Frame(self.master, borderwidth=2)
        self.over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self.over_frame, text="¡Game Over!", font=("Helvetica", 30, "bold"),
                 bg="red", fg="white").pack()


        
    def compute_score(self, board):
        """Calcula el puntaje total del tablero sumando todos los valores."""
        return sum(sum(row) for row in board)