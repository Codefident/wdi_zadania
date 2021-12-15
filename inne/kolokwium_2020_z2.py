def C(n):
    ns = str(n)
    new_n = ''
    for i in range(len(ns)):
        if ns[i] in '02468':
            new_n += str(int(ns[i]) + 1)
        else:
            new_n += ns[i]
    return int(new_n)


def rek(x, y, n, i, last):
    if x == y and i <= n:
        return 1
    if i == n or i > n:
        return 0

    res = 0
    if last != 'A':
        res += rek(x + 3, y, n, i + 1, 'A')
    if last != 'B':
        res += rek(x * 2, y, n, i + 1, 'B')
    if last != 'C':
        res += rek(C(x), y, n, i + 1, 'C')

    return res


def wrapper(x, y, n):
    return rek(x, y, n, 0, '')

print(wrapper(11, 31, 4))