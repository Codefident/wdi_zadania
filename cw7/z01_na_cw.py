class Node:
    def __init__(self):
        self.val = None
        self.next = None


def member(first, el):
    p = first
    while p != None:
        if p.val == el:
            return True
        p = p.next
    return False