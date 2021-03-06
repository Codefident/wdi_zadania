# Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
# zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.


import math


def sameDigits(a, b):
    a_len = math.floor(math.log10(a)) + 1
    b_len = math.floor(math.log10(b)) + 1

    if a_len != b_len:
        return False
    
    # if a == b:
    #     return

    a_digits = [0 for _ in range(10)]
    b_digits = [0 for _ in range(10)]

    while a > 0:
        a_digits[a % 10] += 1
        a //= 10

    while b > 0:
        b_digits[b % 10] += 1
        b //= 10

    for i in range(a_len):
        if a_digits[i] != b_digits[i]:
            return False
    return True


n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
print(sameDigits(n1, n2))
