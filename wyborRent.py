
class Wybor:
    def __init__(self):
        self.__nr = 0

    def prosOdaneKlientaIroweru(self):
        self.__nr = None
        while self.__nr != 1 and self.__nr != 2 and self.__nr != 3 and self.__nr != 4 and self.__nr != 5:
            print("1 - wprowadz dane klienta")
            print('2 - zapisz klienta')
            print("3 - sprawdź dane, które właśnie wprowadziłeś")
            print('4 - wyświetl całą baze klientów')
            print("5 - zakończ")

            self.__nr = int(input("podaj nr opcji:\n"))

    def opcjaWprowadzDane(self):
        return self.__nr == 1

    def zapiszKlienta(self):
        return  self.__nr == 2

    def wyswietlKlienta(self):
        return  self.__nr == 3

    def wyświetlCalaBazeKlientow(self):
        return self.__nr == 4

    def zakoncz(self):
        return self.__nr != 5