# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.

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
for i in range(2, 36, 3):
    p.next = Node(i)
    p = p.next


def divideList(h):
    lists = [[None, None] for _ in range(10)]
    
    ht = h

    while ht != None:
        i = ht.value % 10
        if lists[i][0] is None:
            lists[i][0] = ht
            lists[i][1] = ht
        else:
            lists[i][1].next = ht
            lists[i][1] = ht
        ht = ht.next
    
    for i in range(9):
        lists[i][1].next = lists[i + 1][0]
    lists[9][1].next = None

    return lists[0][0]


ll = divideList(ll)
printList(ll)