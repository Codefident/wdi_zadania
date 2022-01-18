# 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.


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
for i in range(2, 5):
    p.next = Node(i)
    p = p.next


def addElem(h, v):
    while h.next is not None:
        h = h.next
    h.next = Node(v)

addElem(ll, 20)
addElem(ll, 14)
printList(ll)