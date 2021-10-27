# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

# taka konwersja gubi zera na końcu lecz to nie problem w tym przypadku
def revNum(num):
    reverse = 0
    while num > 0:
        reverse = (reverse * 10) + (num % 10)
        num = num // 10
    return reverse

# to do poprawy
def toBin(num):
    binary = 0
    while num > 0:
        binary = binary*10 + num%2
        num = num // 2
    return binary


n = int(input())
print(revNum(n))
if n == revNum(n):
    print("Ta liczba jest palindromem")
else:
    print("Ta liczba nie jest palindromem")

print("W systemie binarnym...", end=" ")
if toBin(n) == revNum(toBin(n)):
    print("Ta liczba jest palindromem")
else:
    print("Ta liczba nie jest palindromem")

print(toBin(n))