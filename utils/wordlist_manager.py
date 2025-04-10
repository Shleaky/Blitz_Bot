import os

def prune_rejected_words(wordlist_path="assets/words.txt", rejected_path="assets/rejected_words.txt"):
    """
    Removes all rejected words from the word list and clears the rejected log.
    """
    if not os.path.exists(rejected_path) or os.path.getsize(rejected_path) == 0:
        print("ℹ️ No rejected words to prune.")
        return

    with open(wordlist_path, 'r') as f:
        words = set(w.strip().lower() for w in f if w.strip())

    with open(rejected_path, 'r') as f:
        rejected = set(w.strip().lower() for w in f if w.strip())

    cleaned = sorted(words - rejected)

    with open(wordlist_path, 'w') as f:
        for word in cleaned:
            f.write(word + "\n")

    open(rejected_path, 'w').close()  # Clear file after pruning

    print(f"🧹 Pruned {len(rejected)} rejected words from word list.")
    print(f"📄 Updated word list now contains {len(cleaned)} words.")
