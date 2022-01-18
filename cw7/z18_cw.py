# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
#ALE NIE DZIAŁA :))))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def printList(h):
    while h.next != None:
        print(h.value, '-->', end=" ")
        h = h.next
    print(h.value)


ll = Node(19)
p = ll
for i in [2, 3, 1, 7, 1, 2, 3, 5, 7, 18, 3, 5, 22]:
    p.next = Node(i)
    p = p.next



def z18(first):
    p = first
    q = None
    flag = None
    while p != None:
        s = p
        t = p.next
        while t != None:
            if p.value == t.value:
                s.next = t.next
                t = t.next
                flag = True # p jest do usunięcia
            else:
                s = s.next
                t = t.next
        if flag:
            # happy path nie ma początku
            q.next = p.next
            p = p.next
        else:
            q = p
            p = p.next
        
printList(ll)
z18(ll)
printList(ll)