# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
# sposób - generowanie liczb od 0 dodając kolejne cyfry


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


result = set()


def buildNum(n, new_n):
    n = str(n)
    l = len(n)

    if len(new_n) == n:
        return

    for i in range(l):

        if len(new_n) == 0: buildNum(n[i + 1:], new_n + n[i])

        else:
            tmp = new_n + n[i]
            if isPrime(int(tmp)):
                print(tmp)
                result.add(int(tmp))
            buildNum(n[i + 1:], tmp)
            
            
buildNum(2784739, "")
result = list(result)
print(sorted(result))
print(len(result))