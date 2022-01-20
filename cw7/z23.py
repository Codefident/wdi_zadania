# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.

from email import header


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
for i in [2, 4, 27, 69, 2, 5, 12, 7]:
    p.next = Node(i)
    p = p.next

p.next = ll.next.next.next.next


def elementsInCycle(h):
    slow = h
    fast = h

    if h.next and h.next.next is None:
        return -1

    slow = slow.next
    fast = fast.next.next

    while fast and fast.next:
        if fast == slow:
            break
        slow = slow.next
        fast = fast.next.next

    if slow != fast:
        return -1

    slow = h

    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow.value

print(elementsInCycle(ll))
    