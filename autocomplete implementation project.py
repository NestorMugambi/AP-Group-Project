class TrieNode:
    # Represents a single node in the trie
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False  # Boolean flag to indicate if the node marks the end of a valid word

class Trie:
    # The main data structure
    def __init__(self):
        self.root = TrieNode()
