# main.py

from utils.screen_capture import capture_grid, extract_tiles
from ocr.letter_detector import extract_letters
from solver.solver import load_dictionary, find_words, score_word
from automation.input_simulator import play_words

def main():
    
    print("🎯 Capturing grid...")
    grid_image = capture_grid()

    print("📸 Extracting tiles...")
    tiles = extract_tiles(grid_image)

    print("🔠 Extracting letters...")
    board = extract_letters(tiles)

    print("✅ Recognized Board:")
    for row in board:
        print(" ".join(row))
        
    #board = extract_letters(tiles)

    # Print recognized board
    #for row in board:
     #   print(" ".join(row))

    # Load word list and find valid words
    trie = load_dictionary("assets/words.txt")
    words = find_words(board, trie)

    print(f"✅ Found {len(words)} valid words:")
    for word, path, score in sorted(words, key=lambda x: (-score_word(x[0]), x[0])):
        print(f"{word:<10} Score: {score:<4} Path: {path}")

    # Sort by score
    
    words = sorted(words, key=lambda x: -x[2])
    
    print("Playing Words...")
    play_words(words, max_words=80)
    print("Board Complete!")

if __name__ == "__main__":
    main()
