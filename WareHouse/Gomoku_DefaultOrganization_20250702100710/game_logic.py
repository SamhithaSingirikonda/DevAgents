'''
Module containing enhanced Gomoku game logic with draw detection and win line tracking.
'''
class Game:
    '''
    Class to manage Gomoku game state and logic.
    '''
    def __init__(self):
        self.board_size = 15
        self.reset()
    def reset(self):
        '''Reset game state.'''
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1  # 1: Black, -1: White
        self.winner = None
        self.winning_line = []
    def place_stone(self, row, col):
        '''Place a stone and check for win/draw. Returns True if valid move.'''
        if self.winner is not None or self.board[row][col] != 0:
            return False
        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.winner = self.current_player
        else:
            if self.is_board_full():
                self.winner = 0  # Draw
            else:
                self.current_player *= -1
        return True
    def check_win(self, row, col):
        '''Check for winning condition from last move and record winning line.'''
        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1)   # Diagonal /
        ]
        player = self.board[row][col]
        for dr, dc in directions:
            count = 1
            stones = [(row, col)]
            for d in [1, -1]:
                r, c = row, col
                while True:
                    r += dr * d
                    c += dc * d
                    if 0 <= r < self.board_size and 0 <= c < self.board_size:
                        if self.board[r][c] == player:
                            count += 1
                            if d == 1:
                                stones.append((r, c))
                            else:
                                stones.insert(0, (r, c))
                        else:
                            break
                    else:
                        break
            if count >= 5:  # Modified to check for 5 or more consecutive stones
                self.winning_line = stones
                return True
        return False
    def is_board_full(self):
        '''Check if board is completely filled.'''
        for row in self.board:
            if 0 in row:
                return False
        return True