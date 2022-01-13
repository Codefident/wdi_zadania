class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


zb = Node(2)
p = zb

for n in range(6, 10):
    p.next = Node(n)
    p = p.next


def isMember(f, value):
    while f != None:
        if f.value == value:
            return True
        f = f.next
    return False


def printList(f):
    print(f.value, end="")
    while f.next != None:
        f = f.next
        print(" --->", f.value, end="")
        

print(isMember(zb, 6))
print(printList(zb))
