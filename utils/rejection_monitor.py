import pytesseract
import cv2
import numpy as np
import mss
import time

from config import settings

# Replace this with coordinates of your total score (relative to screen)
SCORE_REGION = {
    "top": settings.SCORE_Y,
    "left": settings.SCORE_X,
    "width": settings.SCORE_WIDTH,
    "height": settings.SCORE_HEIGHT
}

def capture_score() -> int:
    """
    Captures and parses the player's current total score.
    """
    with mss.mss() as sct:
        img = np.array(sct.grab(SCORE_REGION))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

        config = "--psm 7 -c tessedit_char_whitelist=0123456789"
        result = pytesseract.image_to_string(thresh, config=config)
        digits = ''.join(filter(str.isdigit, result))

        return int(digits) if digits else 0

def word_was_accepted(prev_score: int, wait_time: float = 0.5) -> bool:
    """
    Compares current score to previous after a word is played.
    """
    time.sleep(wait_time)
    new_score = capture_score()
    return new_score != prev_score
