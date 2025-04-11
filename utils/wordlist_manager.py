from utils.file_loader import load_rejected_words, save_rejected_word

# This list should be populated during runtime by tracking which words failed to score
FAILED_WORDS_THIS_ROUND = []

def mark_rejected_word(word: str):
    """
    Add a word to the current round's rejected list.
    """
    word = word.upper()
    if word not in FAILED_WORDS_THIS_ROUND:
        FAILED_WORDS_THIS_ROUND.append(word)

def prune_rejected_words():
    """
    Save all rejected words from the round into the persistent rejected words file.
    """
    for word in FAILED_WORDS_THIS_ROUND:
        save_rejected_word(word)
    print(f"🧹 Pruned {len(FAILED_WORDS_THIS_ROUND)} rejected words to file.")
    FAILED_WORDS_THIS_ROUND.clear()
