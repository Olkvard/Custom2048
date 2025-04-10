# config.py
# -------------------------
# Configuración del juego y estilo
# -------------------------

# Tamaño del tablero: número de filas y columnas
BOARD_SIZE = 3

# Colores de las casillas según su valor.
# Puedes extender o modificar los colores según tus gustos.
TILE_COLORS = {
    0: "azure4",          # Casillas vacías
    2: "lightgoldenrod",
    4: "orange",
    8: "tomato",
    16: "red",
    32: "purple",
    64: "blue",
    128: "green",
    256: "yellow",
    512: "pink",
    1024: "brown",
    2048: "gold"
}

# Configuración de la fuente: nombre, tamaño y estilo.
FONT_SETTINGS = ("Helvetica", 24, "bold")

# Dimensiones de cada celda en la interfaz (ajusta ancho y alto a tu preferencia).
CELL_WIDTH = 4
CELL_HEIGHT = 2
