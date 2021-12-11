# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

# T = [1, 7, 3, 5, 11, 2]
T = [1, 2, 3, 4, 5, 2]


def min_sum(T, sn, si, i):
    if i == -1:
        if sn * si == 0 or sn != si:
            return 0
        return sn

    response = min_sum(T, sn, si, i - 1)  # skip current element
    if response > 0:
        return response

    return min_sum(T, sn + T[i], si + i, i - 1)  # take current element


print(min_sum(T, 0, 0, len(T) - 1))
