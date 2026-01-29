'''
Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną. 
Funkcja ma wyświetlić ile wynosi podana liczba w zapisie binarnym.

42 = 101010
'''

def binary(a):
      wynik = ''
      while a != 0:
            m = a % 2
            a = a // 2
            wynik = str(m) + wynik
      print(wynik)

binary(42)
