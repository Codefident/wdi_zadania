def czyIstniejePodciag(suma):
    p1 = 1
    p2 = 1
    
    handle_suma = 0
    x = p1
    y = p2
    ciag = ""
    while handle_suma <= suma:
        ciag += " " + str(x)
        handle_suma += x
        if handle_suma == suma:
            print(ciag)
            return "istnieje"

        ciag += " " + str(y)
        handle_suma += y
        if handle_suma == suma:
            print(ciag)
            return "istnieje"

        x = x + y
        y = x + y
    
    # odejmowanie
    while handle_suma >= suma:
        handle_suma -= p1
        if handle_suma == suma:
            print(p2, (p1+p2))
            return "istnieje"
        pom = p1
        p1 = p2
        p2 += pom
    return "nie istnieje"


suma = int(input("wpisz sume: "))
print(czyIstniejePodciag(suma))
