# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.


T = [2, 1, 13, 12, 29, 20, 30]
prime = [True for _ in range(max(T) + 1)]


def sieve():
    i = 2
    n = len(prime) - 1
    prime[0] = False
    prime[1] = False

    while i**2 <= n:
        if prime[i] == True:
            j = 2
            while j*i <= n:
                prime[j*i] = False
                j += 1
        i += 1


def check(n, d, w):
    if n == 1:
        return w
    if n % d == 0:
        for i in range(d + 1, len(prime)):
            if prime[i]:
                return check(n // d, i, w + 1)
        return w + 1
    else:
        for i in range(d + 1, len(prime)):
            if prime[i] and n % i == 0:
                return check(n // i, i + 1, w + 1)
    return w


def canMakeSubsets(T):
    sieve()
    w_all = [None, None, None]

    for num in T:
        w = check(num, 2, 0)
        if w not in w_all and None in w_all:
            if w_all[0] is None:
                w_all[0] = w
            elif w_all[1] is None:
                w_all[1] = w
            elif w_all[2] is None:
                w_all[2] = w
        elif w not in w_all:
            print(w_all, w)
            return False

    if None in w_all:
        print(w_all)
        return False
    print(w_all)
    return True


print(canMakeSubsets(T))
