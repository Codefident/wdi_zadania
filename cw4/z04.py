# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

def biggestQuotient(t):
    t_size = len(t)

    # biggest col/line
    max_sum = 0 # col
    c_index = 0
    min_sum = None # line
    l_index = None

    # sum for every column
    for c in range(t_size):
        sum = 0
        for l in range(t_size):
            sum += t[l][c]
        if sum > max_sum:
            max_sum = sum
            c_index = c

    # sum for every line
    for l in range(t_size):
        sum = 0
        for c in range(t_size):
            sum += t[l][c]
        if (min_sum is None or sum < min_sum) and sum > 0:
            min_sum = sum
            l_index = l

    print(str(max_sum) + ' / ' + str(min_sum))
    return (l_index, c_index)


t = [
    [1, 1, 7, 9],
    [11, 31, 79, 3],
    [55, 13, 318, 761],
    [78, 8, 0, 470]
]
print(biggestQuotient(t))
