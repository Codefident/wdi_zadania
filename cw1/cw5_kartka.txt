epsilon = 0.001

s = float(input())
a = 1.0
b = 0.0

while abs(a - b) > epsilon:
    b = a
    a = (s/a + a)/2

print(a)