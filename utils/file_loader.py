import os
import sys

def get_asset_path(relative_path: str) -> str:
    """
    Resolves the full path to an asset, supporting both PyInstaller (.exe) and normal script execution.
    """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def load_word_list(file_name: str = "assets/words.txt") -> list:
    """
    Loads a list of words from the given asset file.
    """
    path = get_asset_path(file_name)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip().upper() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Critical: Missing required file: {file_name}")
        input("🔧 Press Enter to exit...")
        sys.exit(1)

def load_rejected_words(file_name: str = "assets/rejected_words.txt") -> list:
    """
    Loads rejected words into memory for pruning or reference.
    """
    path = get_asset_path(file_name)
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return [line.strip().upper() for line in f if line.strip()]

def save_rejected_word(word: str, file_name: str = "assets/rejected_words.txt"):
    """
    Appends a rejected word to the log file.
    """
    path = get_asset_path(file_name)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{word.upper()}\n")

def prune_rejected_words_from_list(word_list: list, rejected_words: list) -> list:
    """
    Removes rejected words from the main word list.
    """
    rejected_set = set(rejected_words)
    return [word for word in word_list if word not in rejected_set]
