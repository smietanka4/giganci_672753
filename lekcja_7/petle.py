# pętla while - pętla dopóki

print("===== ZADANIE 1 =====")

'''
Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli na ekranie
dokładnie tyle komunikatów “Giganci Programowania”. 

1. Program ma poprosić użytkownika o podanie liczby całkowitej za pomocą funkcji input
2. Za pomocą pętli while, program ma wyświetlić dokładnie tyle samo komunikatów co liczba "Giganci Programowania" 
'''

liczba = int(input("Wprowadź liczbę: "))

while liczba > 0:
      print("Giganci Programowania")
      liczba -= 1

print("===== ZADANIE 2 =====")

import time

print("Start")
time.sleep(1) # Usypianie konsoli na podany w sekundach czas
print('Koniec')

'''
Przekształć poprzednie rozwiązanie tak aby po wpisaniu liczby przez użytkownika
program wypisywał kolejne liczby co sekunde, aż do zera. Po tym w konsoli powinien pojawić się
napis “BOOM!”.
'''

liczba = int(input("Wprowadź liczbę: "))

while liczba > 0:
      print(liczba)
      liczba -= 1
      time.sleep(1)
print("BOOM!")

print("===== ZADANIE 3 =====")
'''
Zgadywanie liczby wylosowanej przez komputer.
Program losuje liczbę, zadaniem użytkownika jest odgadnąć ją. 
Komputer odpowiada “za mało”, “za dużo” lub w przypadku trafienia wyświetla informację o
wygranej i liczbie tur potrzebnych do wygranej.
Zaczynamy od importu modułu random, dzięki któremu komputer będzie mógł
wylosować liczbę. Dodajemy zmienną przechowującą wylosowaną liczbę.
'''

# Import modułu
import random

# Wylosowanie liczby i zapisanie jej do zmiennej
wylosowana_liczba = random.randint(1, 100)

# Zmienne używane do kontroli działania programu
licznik_tur = 0
odpowiedz = 0

while odpowiedz != wylosowana_liczba:
      odpowiedz = int(input("Podaj odpowiedź: "))
      licznik_tur += 1

      if odpowiedz < wylosowana_liczba:
            print("za mało ;p")
      elif odpowiedz > wylosowana_liczba:
            print("za dużo ;b")

print("Gratulacje udało Ci się odgadnąć wylosowaną liczbę!")
print(f"Liczba: {wylosowana_liczba}")
print(f"Ilość tur: {licznik_tur}")







