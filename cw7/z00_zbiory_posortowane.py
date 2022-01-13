class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


class Zbior:
    def __init__(self):
        self.first = None


def insert(z, el):
    n = z.first
    m = None

    while n != None and n.val < el:
        m = n
        n = n.next

    if n != None and n.val == el:
        return

    e = Node(el)
    if m != None:
        m.next = e
        e.next = n
        return
    e = z.first
    z.first = e
    return