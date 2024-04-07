"""
LinkedList script.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """
    Parse a linked list from a string.
    """
    split_lst = s.split(' -> ')
    numbers = []
    for ind, elem in enumerate(split_lst):
        if ind != len(split_lst)-1:
            numbers.append(int(elem))
    head = None
    for num in reversed(numbers):
        head = Node(num, head)
    return head
