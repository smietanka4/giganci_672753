# '''
# Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy
# średnią z przedmiotu.

# N - liczba ocen wprowadzona przez użytkownika na początku działania programu

# Dodatkowa część:
# Następnie wyświetli ocenę końcową z przedmiotu jako zaokrąglenie średniej do całości.
# '''

# n = int(input("Podaj liczbę ocen do wpisania: "))
# suma = 0

# for ocena in range(1, n+1):
#       ocena_czastkowa = int(input(f"Podaj ocenę nr {ocena}: "))
#       suma += ocena_czastkowa

# srednia = suma / n
# print("Twoja średnia wynosi: ", srednia)

# print("===== Ulepszone zadanie =====")

# '''
# Obliczanie średniej z wprowadzonych ocen.
# Program musi wczytywać oceny, aż napotka znak 'q' mówiący, że wprowadzono
# wszystkie oceny. Idealne miejsce na wykorzystanie pętli while.
# '''

# oceny = []

# while True:
#       ocena = input("Podaj ocenę albo wpisz 'q' aby zakończyć: ")

#       if ocena == 'q':
#             break
#       else:
#             ocena = float(ocena)
#             oceny.append(ocena)

# suma = sum(oceny)
# srednia = suma / len(oceny)
# print("Twoja średnia wynosi: ", srednia)

# print("===== Zadanie =====")

# '''
# Odwrócenie wprowadzonych komunikatów.
# Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od
# użytkownika tyle komunikatów. 
# Na koniec wyświetli je w tej samej kolejności.

# 1. Program ma zapytać o liczbę elementów
# 2. Tworzymy liste elementów
# 3. Tworzymy pętlę, która przyjmie tyle komunikatów ile podana liczba elementów
# 4. Wyświetlamy elementy w odpowiedniej kolejności 

# Przykładowe działanie:
# Wejście: Siema, Jestem, Karol

# elementy = [Siema, Jestem, Karol]
#                 0,    1,     2
# Wyjście:
# Siema 
# Jestem 
# Karol 
# '''

# liczba_komunikatow = int(input("Podaj liczbę komunikatów: "))
# elementy = []

# for i in range(liczba_komunikatow):
#       komunikat = input(f"Podaj komunikat numer {i}: ")
#       elementy.append(komunikat)

# for index in range(len(elementy)):
#       print(elementy[index])


'''
Napisz program, który wymnoży ze sobą wszystkie elementy w liście. Lista ma zawierać
tylko liczby (int lub float).
'''

print("===== Zadanie =====")
liczby = [5, 6, 7, 5.23, 4.2, 0.1]
wynik = 1

# Podstawowa wersja
# for liczba in liczby:
#       wynik = wynik * liczba

# Wersja rozszerzona żeby iść po indeksach
for index in range(len(liczby)):
      wynik = wynik * liczby[index]

print(wynik)















