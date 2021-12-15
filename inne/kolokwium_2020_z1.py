MAX1 = 2
MAX2 = 3

tab1 = [[696, 214],
        [420, 1]]

tab2 = [[511, 174, 189],
        [179, 164, 304],
        [716, 139, 501]]


def getFiveEven(n):

    evenDigits = 0

    while n > 0:
        if (n % 5) % 2 == 0:
            evenDigits += 1
        n //= 5

    return evenDigits


def isFiveEven(tab1, tab2):
    t1 = [[0 for _ in range(MAX1)] for _ in range(MAX1)]
    t2 = [[0 for _ in range(MAX2)] for _ in range(MAX2)]

    for r in range(MAX2):
        for c in range(MAX2):
            if r < MAX1 and c < MAX1:
                t1[r][c] = getFiveEven(tab1[r][c])
            t2[r][c] = getFiveEven(tab2[r][c])


isFiveEven(tab1, tab2)
