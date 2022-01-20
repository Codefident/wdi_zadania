# 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
# jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
# leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
# oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
# czy w wyniku operacji moc zbioru uległa zmianie.


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


def printList(h):
    while h.next != None:
        print(h.value, '-->', end=" ")
        h = h.next
    print(h.value)


ll = Node("Adda")
p = ll
for i in ["Beret", "Bozenka", "Dudu", "Emilka", "Jupik", "Zuzia"]:
    p.next = Node(i)
    p = p.next


def addText(h, text):
    moc_1 = 0
    moc_2 = 1 # bo druga petla nie uwzglednia ostatniego elementu
    added = False
    t = h

    # obliczenie wyjsciowej mocy zbioru
    while t is not None:
        moc_1 += 1
        t = t.next

    t = h
    # dodawany napis powinien rozpoczynac liste
    if t.value > text:
        added = True
        h = Node(text)
        h.next = t
        moc_2 += 1

    while t.next is not None:
        moc_2 += 1
        if t.next.value > text and not added:
            nt = t.next
            t.next = Node(text)
            t.next.next = nt
            added = True
        t = t.next
    if not added:
        t.next = Node(text)
    print(moc_1, moc_2)
    return (moc_1 == moc_2, h)
            
    
printList(ll)
response, ll = addText(ll, "Aadzana")
printList(ll)
print(response)
