import pyautogui
import time
from typing import List, Tuple
from config import settings
from utils.rejection_monitor import capture_score, word_was_accepted

Position = Tuple[int, int]

def tile_to_screen_coords(row: int, col: int) -> Tuple[int, int]:
    """
    Converts a tile grid position to actual screen coordinates.
    """
    x = settings.GRID_X + col * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    y = settings.GRID_Y + row * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    return x, y

def play_word(path: List[Position], delay: float = 0.02):
    """
    Simulates mouse drag from the first to last tile in the path.
    """
    if not path:
        return

    start_x, start_y = tile_to_screen_coords(*path[0])
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()

    for row, col in path[1:]:
        x, y = tile_to_screen_coords(row, col)
        pyautogui.moveTo(x, y, duration=delay)

    pyautogui.mouseUp()

def play_words(words: List[Tuple[str, List[Position], int]], max_words: int = 10, delay: float = 0.02):
    """
    Plays words using real mouse input and logs rejections for feedback learning.
    """
    print(f"🖱️ Playing top {min(max_words, len(words))} words...\n")

    for i, (word, path, score) in enumerate(words[:max_words]):
        print(f"{i+1:>2}. {word:<10} Score: {score:<4} Path: {path}")

        previous_score = capture_score()

        play_word(path, delay=delay)
        time.sleep(0.5)  # Let game update the score

        if not word_was_accepted(previous_score):
            print(f"❌ Rejected: {word}")
            with open("assets/rejected_words.txt", "a") as f:
                f.write(word + "\n")
        else:
            print(f"✅ Accepted: {word}")

        time.sleep(0.3)
