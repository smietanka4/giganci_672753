print("===== ZADANIE ROZGRZEWKOWE =====")
'''
Napisz program, który będzie pytać użytkownika o liczby i zliczać ich sumę, aż do
wprowadzenia przez użytkownika hasła “koniec”.

Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych
ocen.
'''
# suma = 0 # ustawiamy zmienną globalną sumy, żeby zliczać liczby

# while True:
#       dane = input('Podaj liczbę (lub wpisz "koniec" aby zakończyć: ') # pamiętajmy że input zawsze zwraca str!!!

#       if dane == 'koniec':
#             print("Koniec programu")
#             break
#       else:
#             suma += float(dane) # dodajemy dane, przy okazji zamieniamy typ na float (liczba zmiennoprzecinkowa)

# print("Suma tych liczb to:", suma)

print("===== Zadanie 1  =====")

# -100 -25 50 125
for liczba in range(-100, 126, 75):
      print(liczba)

print("===== Zadanie 2 =====")

'''
Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od
Twojego roku urodzenia. Program powinien wykorzystać zmienną wiek oraz pętle for z
instrukcją range.

1. Użytkownik ma podać wiek
2. Pętla for z instrukcją range, która będzie wyświetlać nasz wiek w kolejnych latach kalendarzowych

Oczekiwany rezultat:
W roku 2006 miałeś/aś 0 lat
W roku 2007 miałeś/aś 1 lat
'''

wiek_rocznikowo = int(input("Podaj swój wiek rocznikowo: "))

for i in range(wiek_rocznikowo+1):
      rok = 2025 - wiek_rocznikowo + i 
      wiek = i
      print(f"W roku {rok} miałeś/aś {wiek} lat")






