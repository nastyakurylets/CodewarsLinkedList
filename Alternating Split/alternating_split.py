"""
Alternating sptit script.
"""
class Node(object):
    """
    Node class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Take one list and divide up its nodes to make two smaller lists.
    """
    if head is None or head.next is None:
        raise AttributeError
    first_head = Node(head.data)
    second_head = Node(head.next.data)
    first_current = first_head
    second_current = second_head
    pointer = head.next.next
    count = 2
    while pointer is not None:
        new_node = Node(pointer.data)
        if count % 2 == 0:
            first_current.next = new_node
            first_current = first_current.next
        else:
            second_current.next = new_node
            second_current = second_current.next
        pointer = pointer.next
        count += 1
    return Context(first_head, second_head)
