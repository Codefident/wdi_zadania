def nwd(a, b):
    while b != 0:
        pom = b
        b = a%b
        a = pom
    return a

x = int(input())
y = int(input())
z = int(input())

print(nwd(x, nwd(y, z)))
