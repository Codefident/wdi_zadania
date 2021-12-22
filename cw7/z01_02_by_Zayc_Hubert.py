# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, data, index):
        self.index = index
        self.data = data
        self.next = None

    def find(self, index):
        if self.next is None:
            return None

        if self.index == index:
            return self.data

        return self.next.find(index)

    def is_inside(self, data):
        if self.data == data:
            return True
        elif self.next is None:
            return False
        else:
            return self.next.is_inside(data)

    def insert(self, data):
        if self.data != data:
            if self.next is None:
                self.next = Node(data)
            else:
                self.next.insert(data)

    def remove(self, data):
        temp = self
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
            temp = temp.next

    def set_index(self, data, index):
        temp = self
        while temp.next is not None and temp.next.index < index:
            temp = temp.next

        if temp.next is not None and temp.next.index == index:
            temp.next.data = data
            return

        created = Node(data, index)

        if temp.next is None:
            temp.next = created
        else:
            temp.next, created.next = created, temp.next

    def __str__(self):
        if self.next is None:
            return str(self.index) + ":  " + str(self.data)
        else:
            return str(self.index) + ":  " + str(self.data) + "\n" + str(self.next)


s = Node(1, 0)
s.set_index(2, 2)
s.set_index(3, 5)
s.set_index(4, 6)
s.set_index(5, 3)

# s.insert(2)
# s.insert(3)
# s.remove(2)
print(s)
