# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


zb = Node(2)
p = zb

for n in [4,8,20,50,100,176,213]:
    p.next = Node(n)
    p = p.next


zb2 = Node(1)
p2 = zb2

for n in [3, 13, 31, 51, 121, 149, 200]:
    p2.next = Node(n)
    p2 = p2.next


def printList(f):
    print(f.value, end="")
    while f.next != None:
        f = f.next
        print(" --->", f.value, end="")
    print()


def scal(f1, f2):
    pom1 = f1
    pom2 = f2

    if f1.value < f2.value:
        f = f1
        pom1 = pom1.next
    else:
        f = f2
        pom2 = pom2.next
    
    p = f

    while pom1 is not None or pom2 is not None:

        while pom1 is not None and pom2 is not None:
            if pom1.value < pom2.value:
                p.next = pom1
                pom1 = pom1.next
            else:
                p.next = pom2
                pom2 = pom2.next
            p = p.next

        while pom1 is not None:
            p.next = pom1
            pom1 = pom1.next
            p = p.next

        while pom2 is not None:
            p.next = pom2
            pom2 = pom2.next
            p = p.next
    
    return f

printList(scal(zb, zb2))
