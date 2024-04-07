"""
Get Nth Node script.
"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Get nth node.
    """
    if not node or index < 0:
        raise ValueError
    if index == 0:
        return node
    if node.next is None:
        raise ValueError
    return get_nth(node.next, index - 1)
