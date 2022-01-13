# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def printList(h):
    while h.next != None:
        print(h.value, '-->', end=" ")
        h = h.next
    print(h.value)


ll = Node(1)
p = ll
for i in range(2, 10):
    p.next = Node(i)
    p = p.next


def reverseList(h):

    this = h.next
    prev = h

    h.next = None

    while this is not None:
        next = this.next
        this.next = prev
        prev = this
        this = next

    return prev


ll_reversed = reverseList(ll)
printList(ll_reversed)