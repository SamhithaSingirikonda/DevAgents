manual.md
```
# Gomoku Game User Manual

## Overview
Gomoku is a classic strategy board game where two players alternate placing stones on a 15x15 grid, aiming to be the first to get five stones in a row (horizontally, vertically, or diagonally). This implementation features a graphical interface with automatic win detection, turn tracking, and game reset capabilities.

## Installation

### Prerequisites
- Python 3.6 or newer
- Tkinter (usually included with Python installations)

### Installation Steps
1. **Download the game files**  
   Obtain the following files from your provider:
   - `main.py`
   - `game_logic.py`

2. **Run the game**  
   Execute the following command in your terminal:
   ```bash
   python main.py
   ```

*Note for Linux users:* If you encounter Tkinter errors, install it separately:
```bash
sudo apt-get install python3-tk
```

## How to Play

### Game Interface
![Interface Description]
1. **Title Bar**: Displays game name
2. **Game Board**: 15x15 grid for stone placement
3. **Status Label**: Shows current player's turn
4. **New Game Button**: Resets the game

### Basic Rules
1. Black always moves first
2. Players alternate placing stones
3. First player to get 5 stones in a row wins
4. Game ends in a draw if board fills completely

### Game Controls
1. **Placing Stones**  
   - Click near any intersection to place your stone
   - Stones snap to nearest grid intersection
   - Invalid clicks (occupied spaces or between lines) are ignored

2. **Game Flow**  
   - Current player's turn is shown in the status bar
   - Winning moves trigger:
     - Red line through winning stones
     - Victory message popup
   - Draw games display a tie notification

3. **Starting New Game**  
   Click "New Game" button at any time:
   - Confirmation dialog appears
   - Board resets after confirmation

## Features
- 🎯 Automatic win detection (5-in-a-row)
- 🖍️ Winning line highlighting
- ♟️ Turn indicator with player colors
- 🔄 Single-click game reset
- 🛑 Proximity-based stone placement
- 📊 Draw game detection
- 🎨 Classic wooden board aesthetic

## Troubleshooting
**Game won't start:**
- Verify Python installation with `python --version`
- Ensure both game files are in the same directory
- Check for error messages in the terminal

**Missing GUI elements:**
- Install Tkinter if not present (see Linux note in Installation)
- Restart application after installation

**Input not working:**
- Click directly near intersections (within 15 pixel radius)
- Wait for game completion before making moves

## License
This software is provided as-is for educational and personal use. Contains standard Python library dependencies only.
```