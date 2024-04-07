"""
Recursive reverse script.
"""
class Node(object):
    """
    Node class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, previous=None):
    """
    Recursively reverses a linked list.
    """
    if head is None:
        return previous
    next_node = head.next
    head.next = previous
    return reverse(next_node, head)
