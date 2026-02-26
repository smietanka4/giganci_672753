'''
Zadanie 1 - FizzBuzz
Celem zadania FizzBuzz jest napisanie programu, który wypisze na
ekranie liczby 1 do 100, lecz zamiast liczb podzielnych przez 3 ma
napisać Fizz, podzielnych przez 5 Buzz, a podzielnych przez 3 i 5 FizzBuzz
'''

# for i in range(1, 101):
#       if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#       elif i % 3 == 0:
#             print("Fizz")
#       elif i % 5 == 0:
#             print("Buzz")
#       else:
#             print(i)

'''
Zadanie 2 - wzór
Napisz program, który wyświetli na ekranie ten wzór:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''

# liczba = int(input("Podaj liczbę: "))
# for i in range(1, liczba+1):
#       print(str(f"{i} ") * i)

'''
Zadanie 3 - min i max
Należy napisać program, który z listy pokaże nam najmniejszą i największą liczbę

Nie używamy funkcji wbudowanych min i max 
'''

lista = [1,3,7,11,2,-6,0]

najmniejsza = lista[0]
najwieksza = lista[0]

for liczba in lista:
      if liczba > najwieksza:
            najwieksza = liczba

      if liczba < najmniejsza:
            najmniejsza = liczba

print("Najwieksza: ", najwieksza)
print("Najmniejsz: ", najmniejsza)

'''
Zadanie 5 - orzeł i reszka
Program będzie polegał na grze w orła i reszkę. Gracz będzie zgadywać
co wypadnie następne, punkty będzie otrzymywać albo gracz, albo
komputer.

Program ma działać dopóki użytkownik nie wpisze "koniec", albo jedna ze stron będzie miała 10 punktów.
'''

import random

gracz = 0
komputer = 0

gra = True

while gra:
      wybor = input("Orzeł czy reszka? (ew. wpisz 'koniec' jak chcesz zakończyć): ")
      if wybor == "koniec":
            gra = False
      elif wybor == "orzeł" or wybor == "Orzeł":
            moneta = "orzeł"
      elif wybor == "reszka" or wybor == "Reszka":
            moneta = "reszka"
      else:
            print("Proszę dokonać prawidłowego wyboru: ")
            continue
      losowanie = random.choice(["orzeł", "reszka"])  
      print("Wynik rzutu: ", losowanie)
      if moneta == losowanie:
            gracz  += 1
      else:
            komputer += 1

      print("Wyniki łącznie: ")
      print(f"Użytkownik {gracz}/10")
      print(f"Komputer {komputer}/10")

      if gracz == 10:
            print("Koniec gry. Gracz wygrywa!")
            gra = False
      if komputer == 10:
            print("Koniec gry. Komputer Wygrywa ;(")
            gra = False



