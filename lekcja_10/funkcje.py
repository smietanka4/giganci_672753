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

powitanie2(5, "Tomek")

# # end=""
print("Witaj", end=" ")
print("Świecie")
print("!")

# # Zamiana argumentów miejscami
def powitanie(imie, lata):
      print("Hej ", imie, f"Pracujesz w naszej firmie już {lata} lata")

powitanie(lata=50, imie="Karol")

# Zwracanie argumentów przez funkcje

def pole_kwadratu(a):
      pole = a*a
      return pole

def objetosc(pole_podstawy, H):
      objetosc = pole_podstawy * H
      print(objetosc)


pole_kwadratu_o_boku_5 = pole_kwadratu(5)

objetosc(pole_kwadratu_o_boku_5, 3)
