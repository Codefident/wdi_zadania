# W.I.P
# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.


N = 8
t = [[0 for _ in range(N)] for _ in range(N)]
jumps = ((-1, 2), (1, 2), (2, 1), (2, -1),
            (1, -2), (-1, -2), (-2, -1), (-2, 1))
cnt = 1
l, c = 0, 0  # start point


def jump(l, c, cnt):
    t[l][c] = cnt
    
    for a, b in jumps:
        if l+a in range(N) and c+b in range(N):
            if t[l+a][c+b] == 0:
                jump(l+a, c+b, cnt+1)

    if cnt < N**2:
        t[l][c] = 0
        return

    else:
        for line in t:
            print("[ ", end="")
            for elem in line:
                print(elem, "\t", end="")
            print(" ]")
        return


jump(l, c, cnt)
