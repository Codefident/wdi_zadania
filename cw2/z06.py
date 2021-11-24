# . Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12

N = int(input())
sm = 1
lg = N
tmp_N = N

i = 2
while i < tmp_N:
    if N % i == 0:
        sm = i
        lg = N // i
        tmp_N = lg
    i += 1

print(sm, '*', lg)
