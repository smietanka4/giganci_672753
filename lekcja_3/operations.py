# # pobranie wartości z konsoli od użytkownika
# # input()

# # warto by jednak to gdzieś zapisać
# x = int(input())
# print(type(x), x)

# # mozemy coś wpisać do inputa
# imie = input("Podaj swoje imię: ")

# Operacje matematyczne

a=6
b=6

print(+a)
print(-a)

# +, -, *, /, %, //, **
print(a+b) 
print(a-b)
print(a * b)
print(a / b) # operator dzielenia zawsze zwraca float
print(a % b) # operator dzielenia modulo, zwraca reszte z dzielenia pierwszej liczby przez druga
print(a // b)
print(a ** b)

print("=========================")

a=3
b=4
# jak zwiększyć liczbę a o 2?
a = a+2
print(a)
# a można szybciej i zgrabniej
a += 2 # to samo co a = a + 2, ale szybciej
print(a)

# +, -, *, /, %, //, **
c = 10

c -= 1 # c = 9
print(c)

c *= 2 # c = 18
print(c)

c /= 3 # c = 6.0
print(c)

c %= 4 # c = 2.0
print(c)

print("==================")

print(True+True) # 2
print(True+False) # 1
print(False+False) # 0
print(3*True) # 3

print("==================")
# operacje na danych typu string

a = "Sześć"
b = "Siedem"

# Konkatenacja stringów
print(b+a)
print("Witaj " + "Gigancie")

print(3*a)
print("test"*3)

tekst = 'tekst'
nowy_tekst = 'nowy '
nowy_tekst += tekst
print(nowy_tekst)

print("==================")

# f-string
n = 10
m = 5

print("Wynik mnożenia", n, 'przez', m, 'to', n*m)

print(f"Wynik dodawania {n} i {m} to {n+m}")

print("==================")
# Funkcje wbudowane

# matematyczne
print(abs(-10)) # wartość bezwzględna, odległość liczby na osi x od 0
print(max(1,2,3,-5,8,2,11)) 
print(min(1,2,3,-5,8,2,9,10))
print(round(3.567)) # zaokraglanie liczby

# iterowalne
print(len("Giganci2025")) # length -> długość 


# Zadanie 1

print("===== ZADANIE 1 =====")

'''
Pobierz od użytkownika imię, nazwisko, rok urodzenia i wypisz na konsolę
informację (dla danych Jan Kowalski, 1996): „Jan Kowalski ma rocznikowo 25 lat.”

Używamy f-stringa
'''

imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

print(f'{imie} {nazwisko} ma rocznikowo {2025 - rok_urodzenia} lat.')













