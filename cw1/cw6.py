def f(x):
    return x**x - 2020


epsilon = 0.01
x1 = -1
x2 = 1

# krance przedzialu
while f(x1) * f(x2) > 0:
    x1 -= 1
    x2 += 1

while abs(x1 - x2) > epsilon:
    if f((x1 + x2)/2) == 0:
        print((x1 + x2)/2)
        break
    if f((x1 + x2)/2) * f(x1) > 0:
        x1 = (x1 + x2)/2
    else:
        x2 = (x1 + x2)/2
print((x1 + x2)/2)
