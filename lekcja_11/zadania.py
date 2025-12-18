print("===== Zadanie 1 =====")

'''
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca
napis, gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego
argumentu.

laczenie('?', ['ala', 'ma', 'kota']) -> 'ala?ma?kota'
'''

def laczenie(oddzielnik, lista):
      # slowo = ""

      # for element in lista:
      #       slowo += element
      #       slowo += oddzielnik
      
      # nowe_slowo = slowo[:-1]

      # return nowe_slowo

      return oddzielnik.join(lista)

print(laczenie("?", ['ala', 'ma', 'kota']))

print("===== Zadanie 2 =====")

'''
Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba, którą chcemy
podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
można dokonać dzielenia, a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.
'''

def podzielna(liczba, dzielnik):
      if dzielnik == 0:
            return "Dzielnik nie może być zerem"
      elif liczba % dzielnik == 0:
            return f"Liczba {liczba} jest podzielna przez {dzielnik}"
      else:
            return f"Liczba {liczba} nie jest podzielna przez {dzielnik}"
      
print(podzielna(2,3))
