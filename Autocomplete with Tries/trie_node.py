from collections import defaultdict


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie

        # using a defaultdict to prevent key errors
        # and return default value for non-existant keys

        self.child_nodes = defaultdict(TrieNode)

        # denotes the last char of a given word
        self.is_end_of_word = False

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []
        for char, node in self.child_nodes.items():
            if node.is_end_of_word:
                suffixes.append(suffix + char)

            if node.child_nodes:
                suffixes += node.suffixes(suffix + char)

        return suffixes
