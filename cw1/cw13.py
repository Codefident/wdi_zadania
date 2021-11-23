def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


def nww(a, b):
    return int(a*b/nwd(a, b))


x = int(input())
y = int(input())
z = int(input())

print(nww(x, nww(y, z)))
