"""
Convert a linked list to a string script.
"""
class Node():
    """
    Node class.
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """
    Convert a linked list to a string.
    """
    string = ''
    if node:
        while node:
            string += f'{str(node.data)} -> '
            node = node.next
        return f'{string}None'
    return 'None'
