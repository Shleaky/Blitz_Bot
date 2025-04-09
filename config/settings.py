# config/settings.py

# Monitor index where the game is running (1 = primary, 2 = second monitor, etc.)
MONITOR_INDEX = 2 # Adjust this to your monitor setup
# Set to 0 to capture the primary monitor


# Grid parameters - adjust after first capture to fine-tune
GRID_X = 590        # X offset from top-left of monitor
GRID_Y = 390         # Y offset from top
GRID_WIDTH = 440      # Width of grid area
GRID_HEIGHT = 440     # Height of grid area
GRID_SIZE = 4         # 4x4 Word Blitz grid
# Working at 80% zoom in the browser
# Adjust these values to fit your screen resolution and game layout

# Tile layout
TILE_SIZE = 100
TILE_GAP = 13

# Output tile folder
TILE_FOLDER = "tiles"
