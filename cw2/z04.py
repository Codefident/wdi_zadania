# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.

N = 1000
i, ans = 0, 0

while 2**i <= N:
    j = 0
    while 2**i * 3**j <= N:
        k = 0
        while 2**i * 3**j * 5**k <= N:
            ans += 1
            k += 1
        j += 1
    i += 1
print(ans)