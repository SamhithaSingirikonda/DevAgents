'''
Main entry point for the Gomoku game application.
Initializes the game logic and GUI components.
'''
import tkinter as tk
from game_logic import GameLogic
from gui import GomokuGUI
def main():
    root = tk.Tk()
    root.title("Gomoku Game")
    game = GameLogic()
    gui = GomokuGUI(root, game)
    root.mainloop()
if __name__ == "__main__":
    main()