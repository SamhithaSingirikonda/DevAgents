'''
Handles graphical user interface for Gomoku game using Tkinter.
Manages board display, user interactions, and game state visualization.
'''
import tkinter as tk
from tkinter import messagebox
from game_logic import GameLogic
class GomokuGUI:
    def __init__(self, master, game):
        '''Initialize GUI components and game bindings'''
        self.master = master
        self.game = game
        self.cell_size = 30
        self.board_size = 15 * self.cell_size
        # Configure styles
        self.bg_color = '#DEB887'  # Wooden background
        self.line_color = '#8B4513'  # Brown lines
        # Create widgets
        self.status_label = tk.Label(master, text="Black's Turn", font=('Arial', 14))
        self.status_label.pack(pady=5)
        self.canvas = tk.Canvas(master, 
                               width=self.board_size, 
                               height=self.board_size, 
                               bg=self.bg_color)
        self.canvas.pack()
        self.reset_button = tk.Button(master, text="New Game", command=self.reset_game)
        self.reset_button.pack(pady=5)
        # Initialize game elements
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
    def draw_board(self):
        '''Draws the 15x15 grid on canvas'''
        self.canvas.delete("all")
        for i in range(15):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.board_size, fill=self.line_color)
            self.canvas.create_line(0, x, self.board_size, x, fill=self.line_color)
    def draw_stone(self, row, col, player):
        '''Draws a stone at specified position'''
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2
        color = "black" if player == GameLogic.BLACK else "white"
        radius = self.cell_size // 3
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                               fill=color, outline="black")
    def on_click(self, event):
        '''Handles player click events'''
        if self.game.game_over:
            return
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < 15 and 0 <= col < 15:
            current_player_before = self.game.current_player
            valid, result = self.game.place_stone(row, col)
            if valid:
                self.draw_stone(row, col, current_player_before)
                if result == 'win':
                    winner = "Black" if current_player_before == GameLogic.BLACK else "White"
                    messagebox.showinfo("Game Over", f"{winner} wins!")
                    self.status_label.config(text="Game Over")
                elif result == 'draw':
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.status_label.config(text="Game Over")
                else:
                    current = self.game.current_player
                    player_text = "Black" if current == GameLogic.BLACK else "White"
                    self.status_label.config(text=f"{player_text}'s Turn")
    def reset_game(self):
        '''Resets the game state and UI'''
        self.game.reset()
        self.draw_board()
        self.status_label.config(text="Black's Turn")