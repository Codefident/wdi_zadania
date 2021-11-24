# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
# różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
# dla 2315 będą to 21, 35, 231, 315.

# rozwiązanie to maska bitowa

import math

N = 2315
DIGITS = math.floor(math.log10(N)) + 1
DIV = 7
LIMIT = 2**DIGITS
cnt = 0

for mask in range(1, LIMIT):
    # 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100 itd.
    print('mask: ', mask)
    a = 0
    tmp_n = N
    n10 = 1 # to make 2, 3..etc digits numbers

    while mask > 0:
        if mask % 2 == 1:
            a += (tmp_n % 10) * n10
            n10 *= 10
        tmp_n //= 10
        mask //= 2

    if a % DIV == 0:
        cnt += 1
    
    print(a)

print(cnt)