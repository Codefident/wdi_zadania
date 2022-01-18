# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


def printList(h):
    while h.next != None:
        print(h.value, '-->', end=" ")
        h = h.next
    print(h.value)


ll = Node(1)
p = ll
for i in range(2, 3):
    p.next = Node(i)
    p = p.next


def removeLastElement(h):
    while h.next.next is not None:
        h = h.next
    h.next = None

removeLastElement(ll)
printList(ll)