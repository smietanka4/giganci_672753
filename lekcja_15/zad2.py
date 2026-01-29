'''
Napisz funkcję, która otrzyma jeden argument określający liczbę binarną. 
Funkcja ma wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.

decimal(101010) = 42
'''

def decimal(a):
      wynik = 0
      i = 0
      while a != 0:
            mod = a % 10
            a = a // 10
            wynik += mod * (2**i)
            i += 1
      print(wynik)

decimal(101010)