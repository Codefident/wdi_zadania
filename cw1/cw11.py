def sumaDz(x):
    suma = 1
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            if i != x/i: #np. 4x4 = 16
                suma += i + (x/i)
            else:
                suma += i
    return suma


a = 1
while a < 10000:
    b = a+1
    while b < 10000:
        if sumaDz(a)==b and sumaDz(b)==a:
            print(a, b)
        b+=1
    a+=1
