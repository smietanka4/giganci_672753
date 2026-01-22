'''
Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
rozrywki i na tej podstawie obliczy koszt transakcji.
Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł
Wyświetl komunikat:
"Cena biletów: XX zł"

XX to wartość liczbowa

Jeśli wprowadzono niepoprawny numer miesiąca program powinien wyświetlić
informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"
'''

ilosc_biletow = int(input("Podaj liczbę biletów: "))
miesiac = input("Podaj miesiąc, w którym chcesz odwiedzić park (styczeń-grudzień) w liczbie: ")
cena_biletu = 0

if int(miesiac) > 12 or int(miesiac) < 1:
      print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie")
elif miesiac == "1" or miesiac == "2" or miesiac == "12":
      cena_biletu = 50
elif miesiac == "3" or miesiac == "4" or miesiac == "10" or miesiac == "11":
      cena_biletu = 100
elif miesiac == "5" or miesiac == "6" or miesiac == "8" or miesiac == "9":
      cena_biletu = 200
else:
      cena_biletu = 250

if cena_biletu > 0:
      print(f"Cena biletów: {ilosc_biletow*cena_biletu} zł")

