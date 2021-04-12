from collections import defaultdict


class RouteTrieNode:
    def __init__(self):
        self.child_nodes = defaultdict(RouteTrieNode)
        self.handler = 'not found handler'
