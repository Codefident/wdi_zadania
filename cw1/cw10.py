# hihi

for x in range(1000001):
    s = 0
    for i in range(1, x): 
        if x % i == 0:
            s += i
    if s == x:
        print(x)