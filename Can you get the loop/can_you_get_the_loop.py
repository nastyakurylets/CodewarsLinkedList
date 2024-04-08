"""
Can you get the loop script.
"""
def loop_size(node):
    """
    Determine the length of the loop.
    """
    visited = set()
    count = 0
    while node not in visited:
        visited.add(node)
        node = node.next
        count += 1
    cycle_start = node
    count = 1
    node = node.next
    while node != cycle_start:
        count += 1
        node = node.next
    return count
