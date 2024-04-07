"""
Swap Node Pairs In Linked List script.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """
    Swap each pair of nodes in the list, 
    then returns the head node of the list.
    """
    if not head or not head.next:
        return head
    second = head.next
    head.next = swap_pairs(second.next)
    second.next = head
    return second
