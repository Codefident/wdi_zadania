import math


def convert(n, s):
    digits = list("0123456789ABCDEF")

    l = math.floor(math.log(n, s)) + 1
    cn = [None for _ in range(l)]

    cn_index = l - 1
    while n > 0:
        cn[cn_index] = (digits[n % s])
        n //= s
        cn_index -= 1
    print(cn)
    for item in cn:
        print(item, end="")


n = int(input("liczba naturalna = "))
s = int(input("...na system: "))
convert(n, s)
