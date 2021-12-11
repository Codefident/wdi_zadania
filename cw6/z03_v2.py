# T = [[6, 7, 6, 6, 8, 6, 1, 6],
#      [6, 3, 2, 9, 8, 3, 6, 6],
#      [2, 6, 2, 8, 2, 6, 5, 9],
#      [9, 3, 3, 3, 9, 1, 5, 7],
#      [9, 7, 9, 8, 9, 1, 1, 8],
#      [1, 2, 6, 6, 9, 6, 7, 9],
#      [1, 9, 5, 5, 2, 2, 8, 9],
#      [2, 9, 5, 8, 2, 9, 5, 7]]

T = [[6, 1, 6, 6, 8, 6, 1, 6],
     [0, 9, 9, 9, 8, 3, 6, 6],
     [8, 9, 0, 8, 2, 6, 5, 9],
     [8, 9, 9, 0, 9, 1, 5, 7],
     [8, 9, 9, 0, 9, 1, 1, 8],
     [8, 9, 9, 0, 9, 6, 7, 9],
     [8, 9, 9, 0, 2, 2, 8, 9],
     [8, 9, 9, 0, 2, 9, 5, 7]]



def trip(T, row, col):
    if row == 7:
        return T[row][col]

    left, middle, right = 1000000, 1000000, 1000000
    score_sum = 0
    if col - 1 >= 0:
        left = trip(T, row+1, col-1)
    if col + 1 <= 7:
        right = trip(T, row+1, col+1)
    middle = trip(T, row+1, col)
    score_sum = min(left, middle, right)
    return score_sum + T[row][col]


print(trip(T, 0, 1))
