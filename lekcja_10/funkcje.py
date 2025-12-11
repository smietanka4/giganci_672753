# Tworzenie funkcji

'''
słowo kluczowe def (define) rozpoczyna deklarację funkcji

argumenty pozwalają nam przekazywać informacje z zewnątrz do funkcji i używać ich w środku funkcji
wzór:
def nazwa_funkcji(argumenty):
      instrukcja funkcji

wywoływanie funkcji:
nazwa_funkcji(ew.argumenty)

''' 

def powitanie(imie, lata):
      print("Hej ", imie, f"Pracujesz w naszej firmie już {lata} lata")

powitanie("Karol", 4)

def drukuj(napis):
      print(napis)

drukuj("Siemanko")

def powitanie2(powtorzenia, imie):
      for i in range(powtorzenia):
            print(f"Hej {imie}!")

powitanie2("Tomek", 5)

'''
Przygotuj funkcję obliczającą pole prostokąta. 
Funkcja ma przyjmować długości boków, a następnie obliczać i
wyświetlać pole figury.
'''