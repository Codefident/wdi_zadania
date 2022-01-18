# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.


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
for i in range(2, 12):
    p.next = Node(i)
    p = p.next


def remove2(h):
    p = h
    while h.next is not None:
        p = h
        h = h.next
        p.next = h.next
        p = p.next
        if h.next is not None:
            h = h.next
    

remove2(ll)
printList(ll)