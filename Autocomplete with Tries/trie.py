from trie_node import TrieNode


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.root
        for char in word:
            node = node.child_nodes[char]
        node.is_end_of_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        if not prefix:
            return None

        prefix = str(prefix)

        node = self.root
        for char in prefix:
            if char in node.child_nodes:
                node = node.child_nodes[char]
            else:
                return None
        return node
