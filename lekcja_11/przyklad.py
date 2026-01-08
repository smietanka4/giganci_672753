# Type hinting -> podpowiadanie typów

def prostokat(a: float, b: float) -> float:
      obwod = 2*a + 2*b
      return obwod

print(prostokat(5, 4))

print("===== Zadanie powtórzeniowe =====")

'''
Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.
Dla liczby 249 otrzymujemy 2+4+9 czyli 15
'''

def suma_cyfr(a: int):
      suma_liczb = 0
      liczba = str(a)

      for znak in liczba:
            suma_liczb += int(znak)

      return suma_liczb

print(suma_cyfr(249))





