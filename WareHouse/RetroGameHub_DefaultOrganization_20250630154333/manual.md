```markdown
# Retro Arcade Catalog - User Manual

🕹️ A classic gaming time machine powered by Python/Flask

## Overview
This web application showcases a curated collection of iconic arcade games from the late 70s/early 80s. Built with a retro terminal aesthetic, it features game descriptions, release years, and genres in an authentic CRT-style interface.

## Main Features
- 📟 Green-on-black CRT display aesthetic
- 🕹️ 5 pre-loaded classic arcade games
- 📅 Release year tracking
- 🎮 Genre categorization
- 💾 Easy data customization via Python files
- 🌟 Animated text effects and retro styling

## Installation

### Prerequisites
- Python 3.6+
- pip package manager

### Steps
1. **Install dependencies**:
   ```bash
   pip install flask
   ```

2. **Download these files**:
   - `main.py`
   - `games_data.py`
   - `styles.py`
   - `templates/index.html`

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Access in browser**:
   ```
   http://localhost:5000
   ```

## Usage Guide

### Basic Operation
1. After starting the server, open your web browser
2. View the scrolling list of classic games
3. Each entry shows:
   - Game title
   - Release year
   - Genre
   - Description
4. Browser features:
   - Automatic dark mode
   - CRT-style text glow
   - Responsive design

### Controls
- **Reload**: Refresh browser to see changes
- **Zoom**: Browser zoom works well with the retro font

## Customization

### Add New Games
1. Open `games_data.py`
2. Add entries to the GAMES list:
   ```python
   {
       'name': 'Your Game',
       'year': 1982,
       'description': 'Game details',
       'genre': 'Genre'
   }
   ```

### Modify Styling
Edit `styles.py` to change:
- Color scheme
- Spacing
- Border effects
Example:
```python
STYLES = {
    'background': '#000055',  # Dark blue background
    'text_color': '#55FF55',  # Brighter green text
    # ... other properties
}
```

## Troubleshooting

### Common Issues
**Port in use**:
```bash
# Stop other instances first
python main.py --port 5001
```

**Missing dependencies**:
```bash
pip freeze | grep Flask  # Verify Flask installation
```

**Style not updating**:
- Clear browser cache with Ctrl+F5

## Technical Support
For assistance, contact:
📧 support@retrocatalog.dev

v1.0 | © 2023 ChatDev Arcade Division
```

This manual provides users with clear installation instructions, usage guidance, and customization options while maintaining the retro theme in its presentation. The CRT-style formatting in markdown helps maintain aesthetic consistency with the application itself.