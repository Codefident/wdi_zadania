def iloczyn(n):
    a = 1
    b = 1
    while a * b <= n:
        if a * b == n:
            return True
        pom = a
        a = b
        b += pom
    return False


print(iloczyn(int(input())))
