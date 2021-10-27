# Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
# ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

a = int(input())
b = int(input())
n = int(input())

print(a//b, end=".")

while n > 0:
    a = (a % b) * 10
    print(a//b, end="")
    n -= 1