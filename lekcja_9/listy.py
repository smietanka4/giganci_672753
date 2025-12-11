# Listy 

oceny = [4,5,2,1,3,6,7]
print(oceny)
print(type(oceny))

moja_lista = [2, "Napis", 'litera', 2.5, -10.67, True, 'a', ["Kolejna", "Lista"], 67]

moja_lista = [
      2, "Napis", 
      'litera', 
      2.5, 
      -10.67, 
      True, 
      'a', 
      ["Kolejna", "Lista"],
       67
]

print(moja_lista)
print(type(moja_lista))

# Ćwiczenie na zapoznanie się ze składnią
# Listy powinny być uporządkowane w sposób zrozumiały dla użytkownika!!

lista_gier = ["Assassin's Creed Unity", "CS:GO", "Terraria", "Helldivers 2"]
print(lista_gier)

lista_osob_1 = [
      ["Igor", "Nowak", 13],
      ["Jola", "Lojalna", 67],
      ["Adam", "Kowalski", 20]
]

print(lista_osob_1)

lista_osob_2 = [
      ["Igor", "Jola", "Adam"],
      ["Nowak", "Lojalna", "Kowalski"],
      [13, 67, 20]
]

# Indeksy - czyli numerowanie elementów
#        0  1  2  3  4  5  6
oceny = [4, 5, 2, 1, 3, 6, 7]

# wyciągnięcie podanego elementu z listy
print(oceny[3])

# przypisane podanego elementu z listy do zmiennej
moja_ocena = oceny[3]
print(moja_ocena)

# zmiana danego elementu z listy na inny
oceny[3] = 5
print(oceny)

# WAŻNE FUNKCJE DO LIST

# len (length) - z ang. długość, po prostu zwraca ilość elementów w liście
dlugosc_listy = len(oceny)
print("Długość listy", dlugosc_listy)

# append - dodawanie elementów do listy na sam koniec
oceny.append(4)
print(oceny)

# sum - sumuje elementy w liście
suma = sum(oceny)
print("Suma: ", suma)

# Pętla for oraz listy

oceny = [4, 5, 2, 1, 3, 6, 7]

# Przechodzenie po elementach listy
for ocena in oceny:
      print(ocena)

print("=============")

# Przechodzenie po indeksach listy
for index in range(len(oceny)):
      print(oceny[index])

# ===== Indeksy CZ.2 =====
print("===== INDEKSY CZ.2 =====")

# Indeksy:   0  1  2  3  4  5  6  7  8    9  10  11   12  13  14
liczby =    [9, 1, 0, 2, 0, 3, 4, 5, 10, -1, 20, 32, -20, -3, -4]
# Indeksy: -15                                                -1

nowa_lista = liczby[-13: -5]
print(nowa_lista)

nowa_lista2 = liczby[2:10]
print(nowa_lista2)

# Odczytywanie elementów z listy - sposób nr.2
oceny_z_3_sprawdzianów = [5, 4.5, 3]
ocena1, ocena2, ocena3 = oceny_z_3_sprawdzianów
print(ocena2)

ocena1, ocena2 = oceny_z_3_sprawdzianów[:2]
print(ocena1)

# ===== Sprawdzanie czy element jest w liście =====
print("======================")

liczby = [5, 6, 7, 5.23, 0.1, 4.2]

if 6 in liczby:
      # Kod wykonywany, jeśli szóstka znajduje się w liście
      print("Jest!")

# ===== Stringi ponowne spojrzenie =====
print("======================")

napis = "Ala ma kota"
print(napis[5])

for litera in napis:
      print(f"Litera: {litera}")

# metoda .join -> pozwala na proste połączenie elementów listy za pomocą konkretnego tekstu

slowa = ["Ala", "ma", "kota"]
tekst = " ".join(slowa)
#       napis.typu_str.join(lista_elementów)
print(tekst)





