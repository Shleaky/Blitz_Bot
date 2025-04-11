import pytesseract
import cv2
import numpy as np
from typing import List
from config import settings
from PIL import Image
import imagehash
import os
import sys

# Tell pytesseract where to find the OCR engine
if settings.TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH

def get_asset_path(relative_path: str) -> str:
    """
    Get the absolute path to a resource, whether running from source or PyInstaller .exe.
    """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

# Known good I tile hash — load from portable-safe location
KNOWN_I_HASH = imagehash.average_hash(Image.open(get_asset_path("tiles/tile_I_reference.png")))

def preprocess_tile(tile: np.ndarray) -> np.ndarray:
    """
    Crops the center of the tile and thresholds it for OCR or hash matching.
    """
    h, w, _ = tile.shape
    crop_x = int(w * 0.25)
    crop_y = int(h * 0.25)
    cropped = tile[crop_y:h - crop_y, crop_x:w - crop_x]
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def is_known_I_tile(tile: np.ndarray) -> bool:
    """
    Compares a tile's image hash to the known I tile.
    """
    # Convert OpenCV image to PIL for hashing
    pil_img = Image.fromarray(tile)
    tile_hash = imagehash.average_hash(pil_img)
    return tile_hash - KNOWN_I_HASH <= 4  # small hash difference = visual match

def extract_letter(tile: np.ndarray) -> str:
    """
    Extracts a single character from a tile using Tesseract OCR.
    Reclassifies ambiguous glyphs and filters intelligently.
    """
    processed = preprocess_tile(tile)

    # No whitelist; allows us to see what Tesseract really returns
    config = "--psm 10 Whitelist: 1|ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = pytesseract.image_to_string(processed, config=config)
    raw = result.strip()

    # Handle common glyphs that look like letters
    raw_upper = raw.upper()

    if raw_upper in ['1', '|']:
        return 'I'
    if raw_upper in ['©', '(', '{', 'c', 'C']:  # Common Tesseract misread for 'C'
        return 'C' 
    if raw_upper == "-":
        print(f"[OCR] Unrecognized tile raw output: '{raw}'")

    # Final filter: accept A-Z only, exactly one char
    letter = ''.join(filter(str.isalpha, raw_upper))
    return letter if len(letter) == 1 else "-"

def extract_letters(tiles: List[np.ndarray]) -> List[List[str]]:
    """
    Converts 16 tile images into a 4x4 list of recognized letters.
    """
    if len(tiles) != settings.GRID_SIZE ** 2:
        raise ValueError("Expected 16 tiles for a 4x4 board.")

    letters = []
    for row in range(settings.GRID_SIZE):
        row_letters = []
        for col in range(settings.GRID_SIZE):
            index = row * settings.GRID_SIZE + col
            letter = extract_letter(tiles[index])
            row_letters.append(letter)
        letters.append(row_letters)
    return letters
