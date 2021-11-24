# Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9,14,15,17,22.
# Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
# następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.

N = int(input())
n = N + 1
while True:
    x, y = 1, 0
    fib_sum = 0
    while fib_sum < n: 
        fib_sum += x
        x, y = x + y, x
    print("\nsuma: ", fib_sum)

    x, y = 1, 0
    while fib_sum > n: 
        fib_sum -= x
        x, y = x + y, x

    if fib_sum != n:
        print(n)
        break
    n += 1