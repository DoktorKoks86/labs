from wyborRent import *
import random
from bike import *
from BikeRepository import *
class Rent:
    def __init__(self, imie, nazwisko, idRoweru, dataOD, dataDO):
        self.imie = imie
        self.nazwisko = nazwisko
        self.idRoweru = idRoweru
        self.dataOD = dataOD
        self.dataDO = dataDO


    def pokazDaneOsobyWypozyczajacej(self):
        print(self.imie, ' ', self.nazwisko, ' ', self.idRoweru, ' ', self.dataOD, ' ', self.dataDO, ' ',)

class RentStory:

    def __init__(self, rejestr):
        self.rejestr = rejestr
        self.tablica = []
        self.counter = 0


    def wprowadzDaneOsoby(self):
        imie = input("podaj imie: \n")
        nazwisko = input("podaj nazwisko: \n")
        idRoweru = input("poda nr idRoweru: \n")
        dataOD = input("poda nr dataOD: \n")
        dataDO = input("poda nr dataDO: \n")

        rent = Rent(imie, nazwisko, idRoweru, dataOD, dataDO)
        self.tablica.append(rent)


    def dodajKlientow(self, clientSource):
        self.tablica.append(clientSource)

    def showClientData(self):
        for clientData in self.tablica:
            clientData.pokazDaneOsobyWypozyczajacej()

    def saveRent(self):
            self.rental = 'wypożyczalnia'
            f = open("c:\source\\" + self.rental + '.txt', 'a')

            for client in self.tablica:
                 self.counter += 1
                 f.writelines(str(self.counter) + ';' + client.imie + ';' + client.nazwisko + ';' + client.idRoweru + ';' + client.dataOD + ';' + client.dataDO + ';' '\n')

            f.close()
            self.tablica = []

def odczytKlientow(rejestr):
        rejestr = 'wypożyczalnia'
        path = "c:\source\\" + rejestr + ".txt"
        f = open(path, 'r')
        content = f.read()
        f.close()

        wyswietlona_bazaRowerow = content.splitlines()
        rentStory = RentStory(rejestr)
        for linia in wyswietlona_bazaRowerow:
            podziel = linia.split(';')
            clientSource = Rent(podziel[0], podziel[1], podziel[2], podziel[3], podziel[4])
            rentStory.dodajKlientow(clientSource)
        return rentStory

addMyClient = RentStory(rejestr='wypożyczalnia')
wyborOpcji = Wybor()
zapisKlienta = None
odczyt = odczytKlientow('wypożyczalnia')
while wyborOpcji.zakoncz():
    wyborOpcji.prosOdaneKlientaIroweru()
    if wyborOpcji.opcjaWprowadzDane():
        addMyClient.wprowadzDaneOsoby()
    if wyborOpcji.wyswietlKlienta():
        addMyClient.showClientData()
    if wyborOpcji.zapiszKlienta():
        addMyClient.saveRent()
    if wyborOpcji.wyświetlCalaBazeKlientow():
        odczyt.showClientData()






