class Node(object):
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Take a list sorted in increasing order and delete any duplicate nodes from the list.
    """
    if head is None:
        return head
    unique_values = set()
    unique_values.add(head.data)
    current = head
    while current.next:
        if current.next.data in unique_values:
            current.next = current.next.next
        else:
            unique_values.add(current.next.data)
            current = current.next
    return head
