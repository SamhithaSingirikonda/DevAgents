'''
Main module for Gomoku GUI application using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from game_logic import Game
class GomokuGUI:
    '''
    Class to handle Gomoku game GUI using Tkinter.
    '''
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.cell_size = 40
        self.board_size = 15
        self.canvas_size = self.cell_size * (self.board_size - 1)
        self.master.title("Gomoku")
        # Add title label
        self.title_label = tk.Label(master, text="Gomoku", font=('Arial', 18, 'bold'))
        self.title_label.pack(pady=10)
        self.canvas = tk.Canvas(master, width=self.canvas_size, height=self.canvas_size, bg='#DEB887')
        self.canvas.pack()
        # Enhanced status label
        self.status_label = tk.Label(master, text="Black's Turn", font=('Arial', 14, 'bold'), 
                                   bg='lightgray', padx=10, pady=5, relief='ridge')
        self.status_label.pack(pady=5)
        self.reset_button = tk.Button(master, text="New Game", command=self.reset_game, 
                                    font=('Arial', 12), bg='#4CAF50', fg='white')
        self.reset_button.pack(pady=5)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)
    def draw_board(self):
        '''Draw the Gomoku board grid with enhanced lines.'''
        for i in range(self.board_size):
            start = self.cell_size * i
            self.canvas.create_line(0, start, self.canvas_size, start, fill='black', width=2)  # Horizontal
            self.canvas.create_line(start, 0, start, self.canvas_size, fill='black', width=2)  # Vertical
    def handle_click(self, event):
        '''Handle player clicks on the board with proximity check.'''
        if self.game.winner is not None:
            return
        col = round(event.x / self.cell_size)
        row = round(event.y / self.cell_size)
        # Check if click is near intersection
        intersection_x = col * self.cell_size
        intersection_y = row * self.cell_size
        dx = event.x - intersection_x
        dy = event.y - intersection_y
        if dx**2 + dy**2 > 15**2:  # 15 pixels radius threshold
            return
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            if self.game.place_stone(row, col):
                self.draw_stone(row, col)
                if self.game.winner is not None:
                    self.show_winner()
                else:
                    player = 'Black' if self.game.current_player == 1 else 'White'
                    self.status_label.config(text=f"{player}'s Turn")
    def draw_stone(self, row, col):
        '''Draw a stone centered at the intersection.'''
        x = col * self.cell_size
        y = row * self.cell_size
        color = 'black' if self.game.current_player == 1 else 'white'
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill=color, outline='black')
    def show_winner(self):
        '''Display winner or draw message and highlight winning line.'''
        if self.game.winner == 0:
            message = "It's a draw!"
        else:
            winner = 'Black' if self.game.winner == 1 else 'White'
            message = f"{winner} wins!"
            # Draw winning line
            if self.game.winning_line:
                start_row, start_col = self.game.winning_line[0]
                end_row, end_col = self.game.winning_line[-1]
                start_x = start_col * self.cell_size
                start_y = start_row * self.cell_size
                end_x = end_col * self.cell_size
                end_y = end_row * self.cell_size
                self.canvas.create_line(start_x, start_y, end_x, end_y, fill='red', width=3)
        messagebox.showinfo("Game Over", message)
        self.status_label.config(text=message)
    def reset_game(self):
        '''Reset the game with confirmation dialog.'''
        if messagebox.askyesno("New Game", "Are you sure you want to start a new game?"):
            self.game.reset()
            self.canvas.delete("all")
            self.draw_board()
            self.status_label.config(text="Black's Turn")
def main():
    root = tk.Tk()
    GomokuGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()