# Konwersje zmiennych

# Konwersja do typu int
a = int(3.6)
print(a, type(a))

# Konwersja do typu bool

c = bool(-1)
print(c, type(c))
c = bool(0)
print(c, type(c))
c = bool(1)

# Konwersja do typu str

d = str(16)
print(d, type(d))
e = str(1.5)
print(e, type(e))
f = str(True)
print(f, type(f))
g = str(False)
print(g, type(g))


# Zadanie

'''
Stworzyć 4 zmienne w których zapiszemy swoje: imię, wzrost (w metrach), wiek (w
latach) i to czy jesteśmy pełnoletni. Następnie wypisujemy je na konsoli (zmienne
powinny być odpowiednio ponazywane). 
'''

imie = "Karol" # -> str
wzrost = 1.84 # -> float
wiek = 19 # -> int
pelnoletniosc = True # -> bool

print(f"Mam na imię {imie}, mój wzrost to {wzrost}. Mam {wiek} lat i jestem pelnoletni ({pelnoletniosc})")

