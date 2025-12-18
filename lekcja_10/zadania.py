print("===== Zadanie 1 =====")

'''
Przygotuj funkcję obliczającą pole prostokąta. 
Funkcja ma przyjmować długości boków, a następnie obliczać i
wyświetlać pole figury.
'''

# def pole_prostokata(a, b):
#       pole = a*b
#       print(f"Pole prostokąta o bokach {a} i {b} jest równe {pole}")

# pole_prostokata(4, 5)

print("===== Zadanie 2 =====")

'''
Napisz funkcję, która przyjmuje dwa argumenty: 
n - liczba powtórzeń, a - liczba startowa. 

Funkcja ma generować kolejne kwadraty liczb, zaczynając od a. Ma
wyświetlić n kolejnych liczb.

kwadrat liczby to liczba * liczba
np. 2*2 = 4 <- kwadrat liczby 2

liczba startowa - 5
liczba powtorzen - 3

Wynik:
5*5 = 25
6*6 = 36
7*7 = 49
'''

def generator_kwadratow(n, a):
      for liczba in range(a, a+n):  
            kwadrat = liczba*liczba
            print(f"{liczba}*{liczba} = {kwadrat}")

generator_kwadratow(a=5, n=3)

print("===== Zadanie 3 =====")
'''
Napisz funkcję tworzącą powitanie, która przyjmuje jako argument imie, a zwraca pełen tekst powitania.
'''

def powitanie(imie):
      return f"Hej {imie}!"

# Jedna wersja, z przypisaniem wyniku funkcji do zmiennej
tekst = powitanie("Karol")
print(tekst)

# Druga wersja, bez przypisywania wyniku funkcji do zmiennej
print(powitanie("Karol"))




