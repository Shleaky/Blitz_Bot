
from typing import List, Set, Tuple
from solver.trie import Trie

Board = List[List[str]]
Position = Tuple[int, int]

DIRECTIONS = [  # 8 directions (including diagonals)
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def load_dictionary(path: str) -> Trie:
    trie = Trie()
    with open(path, 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) >= 3:  # Word Blitz ignores short words
                trie.insert(word)
    return trie

def find_words(board: Board, trie: Trie) -> List[Tuple[str, List[Position]]]:
    found = []
    visited = [[False] * 4 for _ in range(4)]

    def dfs(r: int, c: int, node: Trie, path: List[Position], word: str):
        if not (0 <= r < 4 and 0 <= c < 4) or visited[r][c]:
            return

        char = board[r][c].lower()
        if char not in node.children:
            return

        visited[r][c] = True
        node = node.children[char]
        path.append((r, c))
        word += char

        if node.is_word:
            found.append((word.upper(), path.copy()))

        for dr, dc in DIRECTIONS:
            dfs(r + dr, c + dc, node, path, word)

        visited[r][c] = False
        path.pop()

    for row in range(4):
        for col in range(4):
            dfs(row, col, trie.root, [], "")

    return found

def score_word(word: str) -> int:
    """
    Scores a word based on Word Blitz rules.
    Assumes word is uppercase.
    """
    length = len(word)
    if length < 3:
        return 0
    elif length == 3:
        return 100
    elif length == 4:
        return 200
    elif length == 5:
        return 300
    elif length == 6:
        return 400
    elif length == 7:
        return 500
    else:
        return 600 + (length - 8) * 100

def find_words(board: Board, trie: Trie) -> List[Tuple[str, List[Position], int]]:
    found = []
    visited = [[False] * 4 for _ in range(4)]

    def dfs(r: int, c: int, node: Trie, path: List[Position], word: str):
        if not (0 <= r < 4 and 0 <= c < 4) or visited[r][c]:
            return

        char = board[r][c].lower()
        if char not in node.children:
            return

        visited[r][c] = True
        node = node.children[char]
        path.append((r, c))
        word += char

        if node.is_word and len(word) >= 3:
            score = score_word(word.upper())
            found.append((word.upper(), path.copy(), score))

        for dr, dc in DIRECTIONS:
            dfs(r + dr, c + dc, node, path, word)

        visited[r][c] = False
        path.pop()

    for row in range(4):
        for col in range(4):
            dfs(row, col, trie.root, [], "")

    # Deduplicate by word, keeping highest score instance
    deduped = {}
    for word, path, score in found:
        if word not in deduped or score > deduped[word][1]:
            deduped[word] = (path, score)

    return [(word, path, score) for word, (path, score) in deduped.items()]
