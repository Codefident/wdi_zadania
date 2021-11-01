def convert(n, s):
    digits = list("0123456789ABCDEF")
    cn = []
    while n > 0:
        cn.append(digits[n%s])
        n //= s
    for i in range(len(cn)-1, -1, -1):
        print(cn[i], end="")


convert(3309, 16)