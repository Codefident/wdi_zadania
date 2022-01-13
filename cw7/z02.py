# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get(self, n, i=0):
        if i != n and self.next is not None:
            return self.next.get(n, i + 1)
        return self.value

    def setv(self, a, n, i=0):
        if i != n and self.next is not None:
            self.next.setv(a, n, i + 1)
        else:
            self.value = a


h = Node(15)
p = h
for i in range(16, 20):
    p.next = Node(i)
    p = p.next

h.setv(69, 2)
print(h.get())
