# pętla for

# składnia pętli for
# for element in object:
#       # Miejsce na kod
#       pass

# Iteracja to powtarzanie tej samej czynności lub operacji.

napis = "sześć siedem"

for literka in napis:
      print(literka)

print("=======")

# Funkcja range
# ITERUJEMY OD ZERA!!!!111!!!

# range(stop)

# wersja 1: podajemy tylko parametr stop
for liczba in range(10):
      print(liczba)

print("===========")

# range(start, stop)
# wersja 2: podajemy parametr start i stop
for liczba in range(5,10):
      print(liczba)

print("===========")

# range(start, stop, step)
#wersja 3: podajemy parametr start, stop i step
for liczba in range(5,20,3):
      print(liczba)

print("===========")

# Zagnieżdżenia

for a in range(5): # zewnętrzna pętla
      print(f"a = {a}") 
      for b in range(20,70,10): # wewnętrzna pętla
            print(f"\tb={b}")



