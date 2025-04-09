import pyautogui
import time
from typing import List, Tuple
from config import settings

Position = Tuple[int, int]

def tile_to_screen_coords(row: int, col: int) -> Tuple[int, int]:
    """
    Converts a tile position (row, col) to screen coordinates (x, y)
    """
    x = settings.GRID_X + col * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    y = settings.GRID_Y + row * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    return x, y

def play_word(path: List[Position], delay: float = 0.02):
    """
    Simulates mouse drag through the tile path to input a word on the game board.
    """
    if not path:
        return

    # Move to the starting tile
    start_x, start_y = tile_to_screen_coords(*path[0])
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()

    for row, col in path[1:]:
        x, y = tile_to_screen_coords(row, col)
        pyautogui.moveTo(x, y, duration=delay)

    pyautogui.mouseUp()

def play_words(words: List[Tuple[str, List[Position], int]], max_words: int = 10, delay: float = 0.02):
    """
    Plays a list of scored words in order using mouse simulation.
    """
    print(f"🖱️ Playing top {min(max_words, len(words))} words...")

    for i, (word, path, score) in enumerate(words[:max_words]):
        print(f"{i+1:>2}. {word:<10} Score: {score:<4} Path: {path}")
        play_word(path, delay=delay)
        time.sleep(0.3)  # Small pause between words
