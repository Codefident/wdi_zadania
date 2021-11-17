# Dana jest tablica T[N][N] wypełniona liczbami CAŁKOWITYMI. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

# problemem tutaj jest fakt, że ujemny licznik i ujemny mianownik również mogą dać największą różnicę

from random import randint

N = 6
NUM_MAX_VALUE = 10
t = [[randint(-NUM_MAX_VALUE, NUM_MAX_VALUE) for _ in range(N)] for _ in range(N)]

for line in t:
    print('[---', end="\t")
    for element in line:
        print(element, end="\t")
    print('---]')
    

def biggestQuotient(t):
    t_size = len(t)

    # biggest col/line

    #positive values
    max_sum_positive = 0 # col
    c_index_positive = 0
    min_sum_positive = None # line
    l_index_positive = None

    #negative values
    max_sum_negative = 0 # col
    c_index_negative = 0
    min_sum_negative = None # line
    l_index_negative = None

    for i in range(t_size):

        # sums for lines and columns
        sum_l = 0
        sum_c = 0

        for j in range(t_size):
            sum_l += t[i][j]
            sum_c += t[j][i]

        if sum_c > max_sum_positive:
            max_sum_positive = sum_c
            c_index_positive = i
        elif sum_c < max_sum_negative:
            max_sum_negative = sum_c
            c_index_negative = i
        
        if (min_sum_positive is None or sum_l < min_sum_positive) and sum_l > 0:
            min_sum_positive = sum_l
            l_index_positive = i
        elif (min_sum_negative is None or sum_l > min_sum_negative) and sum_l < 0:
            min_sum_negative = sum_l
            l_index_negative = i

    if ( max_sum_positive / min_sum_positive ) > ( max_sum_negative / min_sum_negative ):
        print(str(max_sum_positive) + ' / ' + str(min_sum_positive))
        return (l_index_positive, c_index_positive)

    print(str(max_sum_negative) + ' / ' + str(min_sum_negative))
    return (l_index_negative, c_index_negative)
    


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
