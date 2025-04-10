import pyautogui
import time
import threading
import keyboard
from typing import List, Tuple
from config import settings
from utils.rejection_monitor import capture_score, word_was_accepted

Position = Tuple[int, int]

# Flags for controlling execution
stop_playing = False
exit_completely = False

def listen_for_keys():
    """
    Runs in a background thread to monitor keypresses.
    Press 's' to stop the play_words loop early.
    Press 'q' to exit the entire script.
    """
    global stop_playing, exit_completely

    while True:
        if keyboard.is_pressed('s'):
            print("\n⏹️  Stop signal received: Ending word playback early.")
            stop_playing = True
            break
        if keyboard.is_pressed('q'):
            print("\n❌ Exit signal received: Terminating program.")
            stop_playing = True
            exit_completely = True
            break
        time.sleep(0.1)

def tile_to_screen_coords(row: int, col: int) -> Tuple[int, int]:
    x = settings.GRID_X + col * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    y = settings.GRID_Y + row * (settings.TILE_SIZE + settings.TILE_GAP) + settings.TILE_SIZE // 2
    return x, y

def play_word(path: List[Position], delay: float = 0.02):
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
    Plays words and allows mid-run control:
    - Press 's' to stop playing more words.
    - Press 'q' to exit the entire script after word phase.
    """
    global stop_playing, exit_completely
    stop_playing = False
    exit_completely = False

    # Start keyboard listener thread
    key_thread = threading.Thread(target=listen_for_keys, daemon=True)
    key_thread.start()

    print(f"🖱️ Playing top {min(max_words, len(words))} words...")
    for i, (word, path, score) in enumerate(words[:max_words]):
        if stop_playing:
            break

        print(f"{i+1:>2}. {word:<10} Score: {score:<4} Path: {path}")

        prev_score = capture_score()
        play_word(path, delay=delay)
        time.sleep(0.5)

        if not word_was_accepted(prev_score):
            print(f"❌ Rejected: {word}")
            with open("assets/rejected_words.txt", "a") as f:
                f.write(word + "\n")
        else:
            print(f"✅ Accepted: {word}")

        time.sleep(0.3)

    key_thread.join(timeout=0.5)