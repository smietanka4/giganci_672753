print("===== Prosty kalkulator =====")

'''
Wróćmy do przykładu z dzieleniem. Nawet proste kalkulatory są w stanie
wykonywać też inne działania. Spróbujmy stworzyć własny kalkulator w Pythonie.

Specyfikacja:

1. Program poprosi użytkownika o podanie pierwszej liczby.
2. Następnie wyświetli możliwe działania matematyczne, które można wykonać:
a. + → dodawanie
b. - → odejmowanie
c. * → mnożenie
d. / → dzielenie
3. Użytkownik wpisuje znak wybranego działania.
4. Program prosi o drugą liczbę.
5. Na końcu program wyświetla wynik obliczenia.
'''

a = float(input("Wprowadź pierwszą liczbę: "))

# Wyświetl dostępne opcje
print("+ dodawanie")
print("- odejmowanie")
print("* mnożenie")
print("/ dzielenie")
symbol_dzialania = input("Wybierz jedną z dostępnych opcji kalkulatora: ")

b = float(input("Wprowadź drugą liczbę: "))
 
if symbol_dzialania == '+':
    wynik = a + b
elif symbol_dzialania == '-':
    wynik = a - b
elif symbol_dzialania == '*':
    wynik = a * b
elif symbol_dzialania == '/':
    if b == 0:
        print("Nie wolno dzielić przez zero!")
        wynik = "Error"
    else:
        wynik = a / b
else:
    print("Wprowadzono niepoprawny symbol")
    wynik = "Error"
 
print(a, symbol_dzialania, b, "=", wynik)
