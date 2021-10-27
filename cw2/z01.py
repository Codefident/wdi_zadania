# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

def czyIloczyn(a):
    x = 1
    y = 1

    while x*x <= a:
        if x*y == a:
            return [True, x, y]
        x = x + y
        y = x + y
    return False


n = int(input())
print(czyIloczyn(n))
