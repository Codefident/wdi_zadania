# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

T = [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def cut(t, n):

    if t == '':
        return isPrime(int(n, 2))

    next_num = False
    if isPrime(int(n, 2)) and len(t) >= 2:
        next_num = cut(t[2:], t[:2])
    continue_num = cut(t[1:], n + t[0])

    return next_num or continue_num


def z05(T):
    t = ""
    for i in range(len(T)):
        t += str(T[i])
    return cut(t[2:], t[:2])


print(z05(T))
