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

    # Recursively collects all words starting from the given trie node (Helper)
    def _find_words_from(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            results.extend(self._find_words_from(child, prefix + char))
        return results
    
    # Adds a word to the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
