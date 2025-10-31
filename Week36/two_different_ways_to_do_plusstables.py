def losning_forslag1():
    """
    Denne metoden bruker kode til å automatisk finne bredde og deretter skrive kode selv.
    Denne ble gått gjennom torsdag 04.09.25
    :return:
    """
    m: int = int(input("Start på intervallet: "))
    n: int = int(input("Slutt på intervallet: "))

    width: int = max(len(str(m + n)), len(str(n + n)))
    print(width)
    print("|", end="")
    for j in range(m, n + 1):
        print(str(j).rjust(width), "|", end="")
    print()

    print("|", end="")
    for _ in range(m, n + 1):
        print("-" * width, "|", end="")
    print()

    for i in range(m, n + 1):
        print("|", end="")
        for j in range(m, n + 1):
            value = i + j
            print(str(value).rjust(width), "|", end="")
        print()
#






def losning_forslag2():
    """
    Denne oppgaven bruker mer hardkode for å løse oppgaven, ikke det vi gikk
    gjennom torsdag 04.09.25, men er kanskje mer lesbart for nye programmerere.
    :return:
    """
    m = int(input("Skriv starttall: "))
    n = int(input("Skriv sluttall: "))

    def get_len(v):
        return len(str(v))

    header = "|"

    for i in range(m, n + 1):
        if get_len(i) >= 2:
            header += f"  {i} |"
        else:
            header += f"   {i} |"
    print(header)

    split = "|"
    for i in range(m, n + 1):
        split += f"-----|"
    print(split)

    for i in range(m, n + 1):
        rad = "|"
        for j in range(m, n + 1):
            v = j + i
            if get_len(v) >= 2:
                rad += f"  {v} |"
            else:
                rad += f"   {v} |"
        print(rad)
#



losning_forslag1()

losning_forslag2()