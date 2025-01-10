class TrieNode:
    # Represents a single node in the trie
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False  # Boolean flag to indicate if the node marks the end of a valid word

class Trie:
    # The main data structure
    def __init__(self):
        self.root = TrieNode()

# Checks if a given word exists in the trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word