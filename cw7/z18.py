# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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
for i in [2, 3, 1, 7, 1, 2, 3, 5, 7, 18, 3, 5, 22]:
    p.next = Node(i)
    p = p.next


def uniq(h):
    p = h
    prev_t = None
    t = None
    del_h = False # usuwanie pierwszego elementu jesli sie powtarza

    while p is not None:
        prev_t = p
        t = p.next

        while t is not None:
            if t.value == p.value:
                del_h = True
                prev_t.next = t.next
            else:
                prev_t = t
            t = t.next

        if del_h:
            h = p.next
            del_h = False

        p = p.next
    return h
    

printList(ll)
ll = uniq(ll)
printList(ll)