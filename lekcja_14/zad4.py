'''
Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z
komunikatów:

- Jesteś pełnoletni/a
- Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia

Zamiast XX powinna pojawić się wartość liczbowa
'''

wiek = int(input("Podaj swój wiek: "))

if wiek >= 18:
      print("Jesteś pełnoletni/a")
else:
      lata_do_pelnoletniosci = 18 - wiek
      print(f"Nie jesteś pełnoletni/a. Brakuje Ci {lata_do_pelnoletniosci} lata do 18 roku życia")