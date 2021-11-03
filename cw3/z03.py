# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

def sieve(n):
    prime = [True for _ in range(n + 1)]

    i = 2
    while i**2 <= n:
        if prime[i] == True:
            j = 2
            while j*i <= n:
                prime[j*i] = False
                j += 1
        i += 1

    for i, item in enumerate(prime):
        if item and i not in (0, 1):
            print(i, end=" ")


n = int(input("n = "))
sieve(n)
