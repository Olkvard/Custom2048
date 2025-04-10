# game_logic.py
import random
from config import BOARD_SIZE

def init_board():
    """Crea el tablero vacío y añade dos números iniciales."""
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """
    Añade un nuevo número (2 o 4) en una celda vacía de forma aleatoria.
    Se utiliza una probabilidad de 90% para el 2 y 10% para el 4.
    """
    empty_cells = [(i, j) for i in range(BOARD_SIZE)
                          for j in range(BOARD_SIZE)
                          if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choices([2, 4], weights=[90, 10])[0]

def compress(row):
    """Desplaza los números a la izquierda eliminando los ceros intermedios."""
    new_row = [num for num in row if num != 0]
    new_row += [0] * (len(row) - len(new_row))
    return new_row

def merge(row):
    """
    Fusiona números adyacentes iguales.
    Por ejemplo, [2, 2, 4, 4] se convierte en [4, 0, 8, 0] antes de volver a comprimir.
    """
    for i in range(len(row) - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move_left(board):
    """Procesa el movimiento hacia la izquierda para cada fila del tablero."""
    new_board = []
    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final = compress(merged)
        new_board.append(final)
    return new_board

def reverse(board):
    """Invierte el orden de los elementos en cada fila."""
    return [row[::-1] for row in board]

def transpose(board):
    """Transpone el tablero intercambiando filas y columnas."""
    return [list(row) for row in zip(*board)]

def move_right(board):
    """Procesa el movimiento hacia la derecha."""
    reversed_board = reverse(board)
    moved_board = move_left(reversed_board)
    return reverse(moved_board)

def move_up(board):
    """Procesa el movimiento hacia arriba."""
    transposed = transpose(board)
    moved_board = move_left(transposed)
    return transpose(moved_board)

def move_down(board):
    """Procesa el movimiento hacia abajo."""
    transposed = transpose(board)
    reversed_board = reverse(transposed)
    moved_board = move_left(reversed_board)
    final_board = reverse(moved_board)
    return transpose(final_board)

def can_move(board):
    """
    Comprueba si existen movimientos posibles.
    Retorna True si hay por lo menos un movimiento (por celda vacía o fusión posible).
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return True
            if j < BOARD_SIZE - 1 and board[i][j] == board[i][j + 1]:
                return True
            if i < BOARD_SIZE - 1 and board[i][j] == board[i + 1][j]:
                return True
    return False