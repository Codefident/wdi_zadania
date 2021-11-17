# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

from random import randint

n = 6
NUM_MAX_VALUE = 10
t = [[randint(0, NUM_MAX_VALUE) for _ in range(n)] for _ in range(n)]

for line in t:
    print('[---', end="\t")
    for element in line:
        print(element, end="\t")
    print('---]')
    

def biggestQuotient(t):
    t_size = len(t)

    # biggest col/line
    max_sum = 0 # col
    c_index = 0
    min_sum = None # line
    l_index = None

    for i in range(t_size):

        # sums for lines and columns
        sum_l = 0
        sum_c = 0

        for j in range(t_size):
            sum_l += t[i][j]
            sum_c += t[j][i]

        if sum_c > max_sum:
            max_sum = sum_c
            c_index = i
        
        if (min_sum is None or sum_l < min_sum) and sum_l > 0:
            min_sum = sum_l
            l_index = i

    print(str(max_sum) + ' / ' + str(min_sum))
    return (l_index, c_index)


t1 = [
    [1, 1, 7, 9],
    [11, 31, 79, 3],
    [55, 13, 318, 761],
    [78, 8, 0, 470]
]

t2 = [
    [1, 2, 12, 42],
    [42, 66, 64, 77],
    [0, 90, 122, 9],
    [2, 0, 777, 123]
]

print(biggestQuotient(t))
