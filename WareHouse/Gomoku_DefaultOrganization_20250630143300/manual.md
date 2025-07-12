manual.md
```
# Gomoku Game

A classic board game implementation for two players, also known as Five in a Row. Players take turns placing stones on a 15x15 grid, aiming to be the first to create an unbroken line of five stones.

## Features

- 🎮 Two-player local gameplay (Black vs White)
- 🖥️ Clean graphical interface with wooden-style theme
- ✅ Win condition detection (horizontal/vertical/diagonal lines)
- 🤝 Draw game recognition
- 🔄 One-click game reset
- 📊 Turn indicator and game status display

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installation)

## Installation

1. **Install Python**  
   Ensure Python is installed on your system:  
   [Download Python](https://www.python.org/downloads/)

2. **Verify Tkinter**  
   Most Python installations include Tkinter. Verify using:  
   ```python -m tkinter```

3. **Download Game Files**  
   Create a directory containing these files:  
   - `main.py`
   - `game_logic.py` 
   - `gui.py`

## How to Play

1. **Starting the Game**  
   Run from command line:  
   ```python main.py```

2. **Game Interface**  
   - **Game Board**: 15x15 grid
   - **Status Bar**: Shows current player's turn
   - **New Game Button**: Resets the game

3. **Gameplay**  
   - Black always plays first
   - Click any intersection to place a stone
   - Players alternate turns
   - Game ends when:
     - A player forms 5-in-a-row (win)
     - All positions are filled (draw)

4. **After Game End**  
   - Click "New Game" button to restart
   - Close window to exit

## Game Rules

1. Players alternate placing stones of their color
2. First player to create 5 consecutive stones wins
3. Stones can be placed in any empty intersection
4. Lines can be horizontal, vertical, or diagonal
5. Game continues until win or full board

## Troubleshooting

**Game won't start**  
- Ensure Python is properly installed
- Verify all game files are in same directory
- Check error messages in terminal

**Missing Tkinter** (Linux users)  
Install separately:  
```sudo apt-get install python3-tk```

**Display issues**  
- Try resizing window
- Restart the game

## Controls

| Action              | Control         |
|---------------------|-----------------|
| Place stone         | Left mouse click|
| New game            | New Game button |
| Exit game           | Close window    |

Enjoy your game of Gomoku! 🎲
```