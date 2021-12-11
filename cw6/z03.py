# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.


from random import randint


SIZE = 8
# T = [[randint(1, 9) for _ in range(SIZE)] for _ in range(SIZE)]
k = 1
moves = ((1, 1), (1, 0), (1, 1))
T = [[6, 7, 6, 6, 8, 6, 1, 6],
[6, 3, 2, 9, 8, 3, 6, 6],
[2, 6, 2, 8, 2, 6, 5, 9],
[9, 3, 3, 3, 9, 1, 5, 7],
[9, 7, 9, 8, 9, 1, 1, 8],
[1, 2, 6, 6, 9, 6, 7, 9],
[1, 9, 5, 5, 2, 2, 8, 9],
[2, 9, 5, 8, 2, 9, 5, 7]]


def move(w, k, s_cost, t):
    global cost
    s_cost += T[w][k]
    if w==7:
        print(w, k, s_cost, t)
    t.append(s_cost)
    if w == 7:
        if s_cost < cost:
            cost = s_cost
        return

    for a, b in moves:
        if k + b in range(SIZE):
            move(w + a, k + b, s_cost, t.copy())


def start(T, k):
    global cost
    cost = 80
    cost_st = T[0][k]
    print(T[0][k])
    for a, b in moves:
        if k + b in range(SIZE):
            move(a, k + b, cost_st, [cost_st])
    print(cost)


for line in T:
    print(line)
start(T, k)
