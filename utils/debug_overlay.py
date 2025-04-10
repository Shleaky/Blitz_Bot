import cv2
import numpy as np
import mss
from config import settings

def draw_debug_overlay():
    """
    Draws rectangles on a screenshot to visualize the game board and score region.
    """
    with mss.mss() as sct:
        monitor = sct.monitors[settings.MONITOR_INDEX]  # 1 = primary
        screenshot = np.array(sct.grab(monitor))

        # Draw board rectangle (blue)
        board_top_left = (settings.GRID_X, settings.GRID_Y)
        board_bottom_right = (
            settings.GRID_X + settings.GRID_WIDTH,
            settings.GRID_Y + settings.GRID_HEIGHT
        )
        cv2.rectangle(screenshot, board_top_left, board_bottom_right, (255, 0, 0), 2)

        # Draw score rectangle (red)
        score_top_left = (settings.SCORE_X, settings.SCORE_Y)
        score_bottom_right = (
            settings.SCORE_X + settings.SCORE_WIDTH,
            settings.SCORE_Y + settings.SCORE_HEIGHT
        )
        cv2.rectangle(screenshot, score_top_left, score_bottom_right, (0, 0, 255), 2)

        # Show the image
        cv2.imshow("Debug Overlay - Press any key to close", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
