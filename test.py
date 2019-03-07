tablica = []
def dodajNr():
    nrRej = 2

    while nrRej >= 0:
        nrRej += 1
        tablica.append(nrRej)
        return tablica
print(dodajNr())