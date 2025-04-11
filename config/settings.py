# config/settings.py

""" import sys
import os
if getattr(sys, 'frozen', False):
    TESSERACT_PATH = os.path.join(sys._MEIPASS, "tesseract", "tesseract.exe")
else:
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe" """

import os
import sys
import shutil

# Prefer system Tesseract if available
TESSERACT_PATH = shutil.which("tesseract")

# Fallback to bundled Tesseract if running as a .exe
if getattr(sys, 'frozen', False) and not TESSERACT_PATH:
    TESSERACT_PATH = os.path.join(sys._MEIPASS, "tesseract", "tesseract.exe")

# Monitor index where the game is running (1 = primary, 2 = second monitor, etc.)
MONITOR_INDEX = 2 # Adjust this to your monitor setup
# Set to 0 to capture the primary monitor


# Grid parameters - adjust after first capture to fine-tune
GRID_X = 592        # X offset from top-left of monitor
GRID_Y = 410         # Y offset from top
GRID_WIDTH = 440      # Width of grid area
GRID_HEIGHT = 440     # Height of grid area
GRID_SIZE = 4         # 4x4 Word Blitz grid
# Working at 80% zoom in the browser
# Adjust these values to fit your screen resolution and game layout

# Tile layout
TILE_SIZE = 100
TILE_GAP = 12

# Output tile folder
TILE_FOLDER = "tiles"

# Adjust based on screen capture
SCORE_X = 645      
SCORE_Y = 285
SCORE_WIDTH = 80
SCORE_HEIGHT = 30

# Optional
DEBUG_MODE = False  # Set to True to enable debug overlay
# Set to False to disable debug overlay

# Game is running on monitor 2, so draw overlay on monitor 1
GAME_MONITOR_INDEX = 2
DEBUG_MONITOR_INDEX = 1