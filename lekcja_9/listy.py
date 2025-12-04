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
