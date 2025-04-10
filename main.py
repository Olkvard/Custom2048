# main.py
import tkinter as tk
from gui import Game2048GUI

if __name__ == '__main__':
    root = tk.Tk()
    game = Game2048GUI(root)
    root.mainloop()
