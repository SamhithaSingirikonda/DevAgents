'''
Contains game logic for Gomoku including:
- Board state management
- Win/draw condition checking
- Player turn management
- Game state tracking
'''
class GameLogic:
    BLACK = 1
    WHITE = 2
    def __init__(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = self.BLACK
        self.game_over = False
    def place_stone(self, row, col):
        '''
        Attempts to place a stone at specified coordinates.
        Returns tuple: (valid_move, game_status)
        where game_status can be 'win', 'draw', or 'continue'
        '''
        if self.game_over or self.board[row][col] != 0:
            return False, None
        player = self.current_player
        self.board[row][col] = player
        if self.check_win(row, col):
            self.game_over = True
            return True, 'win'
        if all(cell != 0 for row in self.board for cell in row):
            self.game_over = True
            return True, 'draw'
        self.current_player = self.WHITE if player == self.BLACK else self.BLACK
        return True, 'continue'
    def check_win(self, row, col):
        '''
        Checks for winning condition in all directions
        Returns True if five consecutive stones are found
        '''
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        player = self.board[row][col]
        for dx, dy in directions:
            count = 1
            # Check positive direction
            x, y = row + dx, col + dy
            while 0 <= x < 15 and 0 <= y < 15 and self.board[x][y] == player:
                count += 1
                x += dx
                y += dy
            # Check negative direction
            x, y = row - dx, col - dy
            while 0 <= x < 15 and 0 <= y < 15 and self.board[x][y] == player:
                count += 1
                x -= dx
                y -= dy
            if count >= 5:
                return True
        return False
    def reset(self):
        '''Resets game state to initial conditions'''
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = self.BLACK
        self.game_over = False