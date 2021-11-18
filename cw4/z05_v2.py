# Dana jest tablica T[N][N] wypełniona liczbami CAŁKOWITYMI. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

# problemem tutaj jest fakt, że ujemny licznik i ujemny mianownik również mogą dać największą różnicę

from random import randint

N = 6
NUM_MAX_VALUE = 10
t = [[randint(-NUM_MAX_VALUE, NUM_MAX_VALUE)
      for _ in range(N)] for _ in range(N)]

for line in t:
    print('[---', end="\t")
    for element in line:
        print(element, end="\t")
    print('---]')


def biggestQuotient(t):
    t_size = len(t)

    # biggest col/line

    sums = {
        'positives': {
            'lines': {
                'sum': None,
                'index': None
            },
            'columns': {
                'sum': 0,
                'index': 0
            }
        },
        'negatives': {
            'lines': {
                'sum': None,
                'index': None
            },
            'columns': {
                'sum': 0,
                'index': 0
            }
        }
    }

    for i in range(t_size):

        # sums for lines and columns
        sum_l = 0
        sum_c = 0

        for j in range(t_size):
            sum_l += t[i][j]
            sum_c += t[j][i]

        if sum_c > sums['positives']['columns']['sum']:
            sums['positives']['columns']['sum'] = sum_c
            sums['positives']['columns']['index'] = i
        elif sum_c < sums['negatives']['columns']['sum']:
            sums['negatives']['columns']['sum'] = sum_c
            sums['negatives']['columns']['index'] = i

        if (sums['positives']['lines']['sum'] is None or sum_l < sums['positives']['lines']['sum']) and sum_l > 0:
            sums['positives']['lines']['sum'] = sum_l
            sums['positives']['lines']['index'] = i
        elif (sums['negatives']['lines']['sum'] is None or sum_l > sums['negatives']['lines']['sum']) and sum_l < 0:
            sums['negatives']['lines']['sum'] = sum_l
            sums['negatives']['lines']['index'] = i

    if (sums['positives']['columns']['sum'] / sums['positives']['lines']['sum']) > (sums['negatives']['columns']['sum'] / sums['negatives']['lines']['sum']):
        print(str(sums['positives']['columns']['sum']) + ' / ' + str(sums['positives']['lines']['sum']))
        return (sums['positives']['lines']['index'], sums['positives']['columns']['index'])

    print(str(sums['negatives']['columns']['sum']) + ' / ' + str(sums['negatives']['lines']['sum']))
    return (sums['negatives']['lines']['index'], sums['negatives']['columns']['index'])


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
