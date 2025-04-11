from utils.file_loader import load_word_list

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def contains(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def build_trie(word_list: list) -> Trie:
    trie = Trie()
    for word in word_list:
        trie.insert(word)
    return trie

def load_dictionary() -> Trie:
    word_list = load_word_list()
    return build_trie(word_list)

def score_word(word: str) -> int:
    # Basic word scoring: letter value + length
    # Modify if needed for bonus tiles later
    letter_scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
        'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
        'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    return sum(letter_scores.get(c.upper(), 0) for c in word) + len(word)

def find_words(board: list, trie: Trie) -> list:
    found = []
    visited = [[False] * 4 for _ in range(4)]

    def dfs(x, y, path, word):
        if x < 0 or y < 0 or x >= 4 or y >= 4:
            return
        if visited[y][x]:
            return

        letter = board[y][x]
        if letter == "-":
            return

        word += letter
        path.append((x, y))

        if not trie.starts_with(word):
            path.pop()
            return

        if trie.contains(word):
            found.append((word, path.copy(), score_word(word)))

        visited[y][x] = True

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    dfs(x + dx, y + dy, path, word)

        visited[y][x] = False
        path.pop()

    for y in range(4):
        for x in range(4):
            dfs(x, y, [], "")

    return found
