# main.py

from utils.screen_capture import capture_grid, extract_tiles
from ocr.letter_detector import extract_letters
from solver.solver import load_dictionary, find_words, score_word
from automation.input_simulator import play_words
from utils.wordlist_manager import prune_rejected_words
from utils.debug_overlay import draw_debug_overlay 
from config.settings import DEBUG_MODE
from automation.input_simulator import exit_completely
from utils.wordlist_manager import prune_rejected_words

def main():
    input("🛑 Press [Enter] to start cheating...")

    print("🎯 Capturing grid...")
    grid_image = capture_grid()

    print("📸 Extracting tiles...")
    tiles = extract_tiles(grid_image)

    print("🔠 Extracting letters...")
    board = extract_letters(tiles)

    print("✅ Recognized Board:")
    for row in board:
        print(" ".join(row))
        
    if DEBUG_MODE:
        draw_debug_overlay()

    
    # Load word list and find valid words
    trie = load_dictionary("assets/words.txt")
    words = find_words(board, trie)
    possiblescore = 0
    print(f"✅ Found {len(words)} valid words:")
    for word, path, score in sorted(words, key=lambda x: (-score_word(x[0]), x[0])):
        possiblescore += score
        
    print(f"Potential Score: {possiblescore} points")

    # Sort by score
    words = sorted(words, key=lambda x: -x[2])
    
    #playing words
    print("🖱️ Playing words...")
    play_words(words, max_words=60)
    print("Board Complete!")
    
    # ... after playing words
    if not exit_completely:
        prune_rejected_words()
    else:
        print("💡 Skipping word pruning due to exit signal.")
    
    # After the round finishes, clean up rejected words
    #print("🧹 Pruning rejected words...")
    #prune_rejected_words()
    

if __name__ == "__main__":
    main()
