rok = 2021
p1 = 1
np1 = None # poczatek ciagu dla najnizszej sumy
np2 = None
suma = None

while p1 < (rok + 1):
    p2 = 1
    while p2 < (rok + 1):
        x = p1
        y = p2
        while x < (rok + 1) and y < (rok + 1):
            x = x + y
            y = x + y
            if x == rok or y == rok:
                if suma is None or p1 + p2 < suma:
                    suma = p1 + p2
                    np1 = p1
                    np2 = p2
        p2 += 1
    p1 += 1

print(np1, np2, suma)
