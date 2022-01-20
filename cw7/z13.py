# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.

from re import L


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
for i in [2, 3, 2, 5, 4, 3, 12, 1]:
    p.next = Node(i)
    p = p.next

def z13(h):
    t = h
    lr = None
    while t.next is not None:
        
        if t.next.value < t.value:
            if lr is not None:
                if t.next.value < lr:
                    lr = t.next.value
                    t.next = t.next.next
                else:
                    lr = None
                    t = t.next
            else:
                lr = t.next.value # zapisanie wartosci jaka usuwamy
                t.next = t.next.next

        else:
            lr = None
            t = t.next


printList(ll)
z13(ll)
printList(ll)
