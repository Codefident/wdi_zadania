import math


def sameDigits(a, b):
    a_len = math.floor(math.log10(a)) + 1
    b_len = math.floor(math.log10(b)) + 1

    if a_len != b_len:
        return False
    
    # if a == b:
    #     return

    a_digits = [i for i in range(10)]
    b_digits = [i for i in range(10)]

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
