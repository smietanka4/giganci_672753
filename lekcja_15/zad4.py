'''
Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem
wyświetlając: „{podane słowo} jest palindromem” lub „{podane słowo} nie jest
palindromem”
'''

def czy_palindrom(napis):
      if napis == napis[::-1]:
            return True
      else:
            return False
      
print(czy_palindrom("sedes"))