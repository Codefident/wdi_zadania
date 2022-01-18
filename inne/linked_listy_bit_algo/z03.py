class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def printList(h):
    while h.next != None:
        print(h.val, '-->', end=" ")
        h = h.next
    print(h.val)


ll = Node(2)
p = ll
for i in [22, 1, 3, 4, 7, 9, 20, 10, 8, 15, 7, 6, 11, 2]:
    p.next = Node(i)
    p = p.next


def repair(p):
    t = p.next
    prev_t = p
    parzysta = False

    if p.val % 2 == 0:
        p_parzysta = True
        parzysta = True
    else:
        p_parzysta = False
    ue = p

    while t is not None:

        if t.val % 2 == 0:
            parzysta = True
            prev_t = t
            t = t.next

        else:

            if p_parzysta:
                
                prev_t.next = t.next
                t.next = p
                p = t
                ue = t
                prev_t = t
                t = t.next
                p_parzysta = False
            
            elif parzysta:
                prev_t.next = t.next
                t.next = ue.next
                ue.next = t
                ue = t
                t = prev_t.next

    return p

printList(ll)
ll = repair(ll)
printList(ll)