# 22. Dana jest lista, która być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def printList(h):
    while h.next != None:
        print(h.value, '-->', end=" ")
        h = h.next
    print(h.value)


ll = Node(1)
p = ll
for i in [2, 4, 27, 5, 2, 5, 12, 7]:
    p.next = Node(i)
    p = p.next

p.next = ll.next.next.next.next

def hasCycle(h):
    slow = h
    fast = h

    slow = slow.next
    fast = fast.next.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

print(hasCycle(ll))
