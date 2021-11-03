# Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

n = int(input())
n += 1 # pierwsza cyfra jest całością

f = [0 for _ in range(n)] # tablica do zliczania 1/d! poprzez kolejne dzielenia
s = [0 for _ in range(n)] # suma, wartość e
f[0] = 1
s[0] = 2


# d to 1/d!
for d in range(2, n):
    r = 0

    # obliczanie kolejnych wartości 1/d!
    for i in range(n):
        f[i] += r*10
        r = f[i] % d
        f[i] //= d

    # sumowanie w tablicy wynikowej
    for i in range(n):
        s[i] += f[i]


p = 0

# odpowiednie przenoszenie "dziesiątek" tak aby w komórkach były tylko pojedyncze cyfry
for i in range(n - 1, -1, -1):
    s[i] += p
    p = s[i] // 10
    s[i] %= 10

# wypisanie
print(s[0], end=".")
for i in range(1, n, 5):
    print(s[i], end="")
    print(s[i+1], end="")
    print(s[i+2], end="")
    print(s[i+3], end="")
    print(s[i+4], end=" ")
