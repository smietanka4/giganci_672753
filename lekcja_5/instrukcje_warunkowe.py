# Konstrukcja if

print("Wykonam się za każdym razem")
warunek = True

if warunek:
    # Kod wykona się tylko wtedy kiedy warunek jest prawdziwy
    print("Warunek był prawdziwy")
    print("Można dodać wiele linijek kodu")

print("Wykonam się za każdym razem, brak wcięcia")

print("===== Zadanie 1 =====")

'''
Stwórzmy prosty program obliczający wynik z dzielenia. Pamiętamy, że nie wolno
dzielić przez zero. To oznacza, że nasz program musi sprawdzić przez jaką liczbę
będzie dzielić i dopiero wtedy wykonać operację dzielenia. 

W pierwszej instrukcji warunkowej sprawdzamy, czy dzielnik jest różny od zera, 
a w drugiej czy dzielnik jest równy zeru.

1. Program ma sie zapytać użytkownika o liczbe, którą chce podzielić (dzielna)
2. Program ma sie zapytać użytkownika o liczbe, którą będzie chciał dzielić (dzielnik)
3. Program ma sprawdzić czy użytkownik przypadkiem nie dzieli przez 0
    a) Jeżeli nie, to printujemy wynik z dzielenia
4. Program ma sprawdzić czy użytkownik dzieli przez 0
    b) Jeżeli tak, program zwraca odpowiedni komunikat
'''

# dzielna = int(input("Wprowadź dzielną: "))
# dzielnik = int(input("Wprowadź dzielnik: "))

# if dzielnik != 0:
#     print(f"Wynik dzielenia to {dzielna/dzielnik}")
# else:
#     print("Pamiętaj cholero, nie dziel przez 0")

# Konstrukcja if-else

warunek = False

if warunek:
    # Nasz kod wykonywany jest, jeśli warunek jest prawdziwy
    pass
else:
    # Nasz kod wykonywany jest, jeśli poprzednie warunki nie zostały spełnione
    print("SIEMA")

print("===== Zadanie 2 =====")

'''
Napisz program, który powie Ci czy dany uczestnik może skorzystać z nowej atrakcji. 

Ograniczenia:
-minimalny akceptowalny wiek to 12 lat
-minimalny akceptowalny wzrost to 130 cm
-maksymalny akceptowalny wzrost to 195 cm

Program zapyta użytkownika o jego wiek i wzrost, a następnie wyświetli komunikat, czy wolno mu skorzystać z atrakcji.

1. Program zapyta uzytkownika o wiek
2. Program zapyta uzytkownika o wzrost
3. Sprawdzi czy wiek jest wiekszy od 12 i czy wzrost jest wiekszy od 130 i zarazem mniejszy od 195
    a) Jeżeli wszystkie spełnione, to wyswietli komunikat o tym że można korzystać z atrakcji
    b) W przeciwnym przypadku: wyświetli komunikat o tym że nie wolno korzystać z atrakcji
'''

wiek = int(input("Podaj swój wiek: "))
wzrost = int(input("Podaj swój wzrost: "))

if wiek >= 12 and wzrost >= 130 and wzrost <= 190:
    print("Wolno skorzystać Ci z atrakcji")
else:
    print("Nie wolno Ci skorzystać z atrakcji")

# Konstrukcja if-elif-else 

warunek = False
warunek2 = True
warunek3 = False

# elif -> else if (w przeciwnym przypadku jeżeli)
if warunek:
    print("warunek 1 jest prawdziwy")
elif warunek2:
    print("warunek 2 jest prawdziwy")
elif warunek3:
    print("warunek 3 jest prawdziwy")
else:
    print("żaden warunek nie był prawdziwy")

print("===== ZADANIE 3 =====")

'''
Jaką liczbę całkowitą wprowadzono: pozytywną, negatywną, czy równą zero?
Liczba może przyjąć tylko jedną z podanych opcji.
Użytkownik ma podać liczbę.
'''

liczba = int(input("Podaj liczbę: ")) # Pobieramy liczbę od użytkownika

if liczba > 0: # Sprawdzamy czy wprowadzona liczba jest większa od 0?
    print("Liczba jest dodatnia")
elif liczba < 0: # Jeżeli pierwszy warunek się nie sprawdził, to przechodzimy dalej i sprawdzamy czy liczba jest ujemna
    print("Liczba jest negatywna") 
else: # W przeciwnym przypadku, czyli jeżeli żaden z powyższych warunków, nie został spełniony
    print("Liczba jest równa zero")








