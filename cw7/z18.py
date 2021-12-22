# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

arr = [1, 2, 3, 2, 5, 4, 2, 3]
first = Node(arr[0])


def printList(l):
    while l.next != None:
        print(l.val)
        l = l.next



def z18(first):
    p = first
    q = None

    while p != None:
        s = p
        t = p.next
        while t != None:
            if p.val == t.val:
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