from route_trie_node import RouteTrieNode
# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self, basic_handler):
        self.root = RouteTrieNode()
        self.root.handler = basic_handler

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            node = node.child_nodes[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part in node.child_nodes:
                node = node.child_nodes[part]
            else:
                return 'not found handler'

        return node.handler
