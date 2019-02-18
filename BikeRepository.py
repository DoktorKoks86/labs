from bike import *

class BikeRepository:


    def __init__(self, nazwa):
        self.tablica = []
        self.nazwa = nazwa

    def dodajRower(self, rower):
        self.tablica.append(rower)

    def wyswietlRowery(self):
        for i in self.tablica:
            i.wyswietlDostepneRowery()






