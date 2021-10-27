def czyIstniejePodciag(suma):
    p1 = 1
    p2 = 1
    while p1 <= suma:
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
        pom = p1
        p1 = p2
        p2 = pom + p2
    return "nie istnieje"


suma = int(input("wpisz sume: "))
print(czyIstniejePodciag(suma))
