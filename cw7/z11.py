# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli 
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.

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
for i in range(2, 6):
    p.next = Node(i)
    p = p.next


def addRem(h, k):
    t = h.next
    prev_t = h

    if h.value == k:
        return t
    
    while t is not None:
        if t.value == k:
            prev_t.next = t.next
            return h
        prev_t = t
        t = t.next
    
    prev_t.next = Node(k)
    return h

printList(ll)
ll = addRem(ll, 10)
printList(ll)