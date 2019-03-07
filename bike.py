class Bike:

   def __init__(self, rodzajRoweru, kolorRoweru, rozmiarKola):
      self.rodzajRoweru = rodzajRoweru
      self.kolorRoweru = kolorRoweru
      self.rozmiarKola = rozmiarKola

   def wyswietlDostepneRowery(self):
      print(self.rodzajRoweru, " ", self.kolorRoweru, " ", self.rozmiarKola)
