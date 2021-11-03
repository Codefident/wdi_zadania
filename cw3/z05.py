# Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.


tab = [None for _ in range(10)]
i = 0

while True:
    w = int(input("a" + str(i + 1) + ": "))
    if w == 0:
        break
    if i < 10:
        tab[i] = w
    elif w > min(tab):
        for j in range(len(tab)):
            if tab[j] == min(tab):
                tab[j] = w
                break
    i += 1

print(min(tab))
