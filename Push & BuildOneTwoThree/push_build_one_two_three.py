"""
Push & BuildOneTwoThree script.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    Push a node.
    """
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """
    Build nodes.
    """
    return push(push(push(None, 3), 2), 1)
