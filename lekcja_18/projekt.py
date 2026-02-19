import random
kosci = [1,1,1,1,1]
nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ['','','','','','']

def rzuc_koscmi(numery_kosci: str):
    for i in numery_kosci:
        index = int(i) - 1
        kosci[index] = random.randint(1,6)

def pokaz_kosci():
    print("--------------------")
    for i in range(len(kosci)):
        print(f"{i+1}. {kosci[i]}")
    print("--------------------")

def pokaz_tabele_punktow():
    print("--------------------")
    for i in range(len(punkty)):
        print(f"{i+1}. {nazwy_punktow[i]}\t{punkty[i]}")
    print("--------------------")


def sprawdz_czy_przerzucamy():
    odp = input("Czy chcesz przerzucić kości? (t/n)")
    if odp == 't' or odp == 'T':
        return True
    else:
        return False
    
def wstaw_punkty():
    pole = int(input("Gdzie chcesz wstawić punkty (podaj numer rubryki): "))
    if punkty[pole-1] == "":
        if 1 <= pole <= 6:
            wstaw_punkty_gorna_tabela(pole)
    else:
        print("Wybrałeś pole, w którym już wstawiłeś punkty!")
        wstaw_punkty()

def wstaw_punkty_gorna_tabela(liczba):
    liczba_punktow = 0
    for kosc in kosci:
        if kosc == liczba:
            liczba_punktow += kosc
    punkty[liczba-1] = liczba_punktow

# LOGIKA GRY
for tura in range(len(punkty)):
    rzuc_koscmi("12345")
    pokaz_tabele_punktow()
    pokaz_kosci() # print(kosci)

    for _ in range(2):
        czy_przerzut = sprawdz_czy_przerzucamy()
        if czy_przerzut:
            kosci_do_przerzutu = input("Wypisz numery kości, które chcesz przerzucić (bez spacji): ")
            rzuc_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break

    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f"Twój wynik to: {sum(punkty)}")

