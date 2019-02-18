from BikeRepository import *
from bike import *
def readBikeRepository(nazwa):
    nazwa = 'rowery'
    path = "c:\source\\" + nazwa + ".txt"
    f = open(path, 'r')
    content = f.read()
    f.close()

    wyswietlona_bazaRowerow = content.splitlines()
    bikeRepository = BikeRepository(nazwa)
    for linia in wyswietlona_bazaRowerow:
        podziel = linia.split(';')
        rower = Bike(podziel[0], podziel[1], podziel[2])
        bikeRepository.dodajRower(rower)
    return bikeRepository


katalogRowerow = readBikeRepository('rowery')

roweryDoWyswietlenia = readBikeRepository('rowery')
while roweryDoWyswietlenia != 0:
    katalogRowerow.wyswietlRowery()
    break

