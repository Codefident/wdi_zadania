# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.

def allDigitsOdd(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n //= 10
    return True


def oddNumbers(t):
    t_size = len(t)

    for l in range(t_size):
        for c in range(t_size):
            if allDigitsOdd(t[l][c]):
                break
        else:
            return False

    return True


t = [
    [1, 2, 12, 42],
    [42, 66, 64, 77],
    [0, 90, 122, 9],
    [2, 0, 777, 123]
]

print(oddNumbers(t))
