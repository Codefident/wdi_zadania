# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
# sposób - cięcie liczby (lecz sprawdzanie niektórych wywoływane jest kilka razy np. 23)


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


def cutNum(n):
    n = str(n)
    l = len(n)

    if l > 2:
        for i in range(l):
            new_n = n[:i] + n[i+1:]
            if isPrime(int(new_n)):
                result.add(int(new_n))
            cutNum(new_n)

cutNum(2784739)
result = list(result)
print(sorted(result))
print(len(result))