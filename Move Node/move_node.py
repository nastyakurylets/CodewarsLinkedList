"""
Move Node script.
"""
class Node(object):
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Move node to the front of the destintation list.
    """
    new_node = Node(source.data)
    new_node.next = dest
    return Context(source.next, new_node)
