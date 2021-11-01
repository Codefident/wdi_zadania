tab = [None for _ in range(10)]
i = 0

while True:
    w = int(input("a" + str(i + 1) + ": "))
    if w == 0:
        break
    if i < 10:
        tab[i] = w
        print(tab)
    elif w > min(tab):
        for j in range(len(tab)):
                if tab[j] == min(tab):
                    tab[j] = w
                    break
        print(tab)
    i += 1

print(min(tab))
print(tab)