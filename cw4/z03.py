# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.


def hasEvenDigit(n):
    if n == 0:
        return True
    while n > 0:
        if (n % 10) % 2 == 0:
            return True
        n //= 10
    return False


def evenLine(t):
    t_size = len(t)

    for l in range(t_size):
        for c in range(t_size):
            if not hasEvenDigit(t[l][c]):
                break
        else:
            return True
    return False

t = [
    [1, 1, 7, 9],
    [11, 31, 79, 3],
    [55, 13, 318, 761],
    [78, 8, 0, 470]
]
print(evenLine(t))