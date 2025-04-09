# utils/screen_capture.py

import mss
import cv2
import numpy as np
import os
from config import settings

def capture_grid():
    with mss.mss() as sct:
        monitor = sct.monitors[settings.MONITOR_INDEX]
        region = {
            "top": monitor["top"] + settings.GRID_Y,
            "left": monitor["left"] + settings.GRID_X,
            "width": settings.GRID_WIDTH,
            "height": settings.GRID_HEIGHT
        }

        screenshot = sct.grab(region)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        return img

def extract_tiles(grid_img):
    os.makedirs(settings.TILE_FOLDER, exist_ok=True)
    tiles = []

    for row in range(settings.GRID_SIZE):
        for col in range(settings.GRID_SIZE):
            x = col * (settings.TILE_SIZE + settings.TILE_GAP)
            y = row * (settings.TILE_SIZE + settings.TILE_GAP)

            tile = grid_img[y:y + settings.TILE_SIZE, x:x + settings.TILE_SIZE]
            tiles.append(tile)

            filename = f"{settings.TILE_FOLDER}/tile_{row}_{col}.png"
            cv2.imwrite(filename, tile)
            print(f"✅ Saved {filename}")

    return tiles
