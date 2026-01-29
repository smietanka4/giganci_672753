'''
Waszym zadaniem jest napisać funkcję, która zwróci informacje prawda/fałsz czy
podana liczba jest liczbą pierwszą

czy_liczba_pierwsza(8) = False
czy_liczba_pierwsza(3) = True
'''

def czy_liczba_pierwsza(a):
      if a <= 1:
            return False
      else:
            for i in range(2, a):
                  if a % i == 0:
                        return False
      return True

print(czy_liczba_pierwsza(8))
print(czy_liczba_pierwsza(3))
