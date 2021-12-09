# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.


from random import randint


SIZE = 8
T = [[randint(1, 10) for _ in range(SIZE)] for _ in range(SIZE)]
k = 1
moves = ((1, 1), (1, 0), (1, 1))
cost = 80


def move(w, k, s_cost):
    s_cost += T[w][k]
    
    if w == 7:
        return s_cost
            
    for a, b in moves:
        if k + b in range(SIZE):
            move(a, k + b, s_cost)


def start(T, k):
    cost_st = T[0][k]

    for a, b in moves:
        if k + b in range(SIZE):
            move(a, k + b, cost_st)


start(T, k)