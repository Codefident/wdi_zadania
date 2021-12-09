# W.I.P
# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.


N = 5
board = [[0 for _ in range(N)] for _ in range(N)]
jumps = ((-1, 2), (1, 2), (2, 1), (2, -1),
            (1, -2), (-1, -2), (-2, -1), (-2, 1))
all_jumps = [None for _ in range(N*N)]
r = len(jumps)
cnt = 1
l, c = 0, 0  # start point


def jump(l, c, cnt):
    board[l][c] = cnt

    for i in range(r):
        a = jumps[i][0]
        b = jumps[i][1]
        if l+a >= 0 and l+a < N and c+b >= 0 and c+b < N:
            if board[l+a][c+b] == 0:
                all_jumps[cnt-1] = i
                jump(l+a, c+b, cnt+1)

    if cnt**2 < N:
        board[l][c] = 0
        all_jumps[cnt-1]
        jump(l-all_jumps[cnt-2][0], c-all_jumps[cnt-2][1], cnt-1)

    else:
        for line in board:
            print("[ ", end="")
            for elem in line:
                print(elem, "\t", end="")
            print(" ]")


jump(l, c, cnt)
