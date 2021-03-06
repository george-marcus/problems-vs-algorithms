from route_trie import RouteTrie


class Router:
    def __init__(self, basic_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        self.trie = RouteTrie(basic_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        path_parts = self.split_path(path)
        self.trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not path:
            return 'not found handler'

        path_parts = self.split_path(path)
        handler = self.trie.find(path_parts)
        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "/":
            return []

        return path.split("/")
