# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.

def spiral(t):
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    l, c = 0, -1 # lines, columns
    limit = len(t) # specifies the max amount of numbers after which we have to change direction
    number = 1

    while number <= len(t)*len(t):
        for s in range(len(steps)):

            if s == 1 or s == 3:
                limit -= 1

            for _ in range(limit):
                l += steps[s][0]
                c += steps[s][1]
                t[l][c] = number
                number += 1

N = 5
t = [[None for _ in range(N)] for _ in range(N)]
spiral(t)
for line in t:
    print(line)