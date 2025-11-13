print("===== Zadanie 1 =====")

'''
Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie
znajduje się jedna z następujących liter lub ciągów znaków:

● litera „a”
● litera „d”
● ciąg znaków „as”
● ciąg znaków „zzz”

Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat, że wyraz zawiera poszukiwany fragment.
Użytkownik ma podać testowany wyraz.

1. Program ma poprosić użytkownika o wprowadzenie wyrazu
2. Program ma sprawdzić za pomocą instrukcji 'if', czy podany wyraz zawiera chociaż jeden poszukiwany fragment
      -> Jeżeli tak to ma wyświetlić odpowiedni komunikat
      -> Jeżeli nie (w przeciwnym przypadku), ma wyświetlić że słowo nie zawiera
'''

wyraz = input("Podaj testowany wyraz: ")

if ("a" or "d" or "as" or "zzz") in wyraz:
      print(wyraz, 'posiada jedno z wyszukiwanych haseł')
else:
      print(wyraz, 'NIE posiada żadnego z wyszukiwanych')

print("===== ZADANIE 2 =====")

'''
Napisz program, który będzie działał jak podstawowy system logowania.

Wykonaj poniższe kroki:
1. Zapisz dane do logowania w zmiennych:
○ LOGIN = "gigant@trener.pl"
○ HASLO = "qwerty"
2. Poproś użytkownika o podanie loginu (za pomocą input()).
3. Poproś użytkownika o podanie hasła (za pomocą input()).
4. Sprawdź, czy wprowadzone dane są zgodne z zapisanymi loginem i hasłem:
○ jeśli tak - wyświetl komunikat: "Poprawnie zalogowano"
○ jeśli nie - wyświetl komunikat: "Niepoprawny login lub hasło"
'''

LOGIN = "gigant@trener.pl"
HASLO = "qwerty"

login_wprowadzony = input("Podaj login: ")
haslo_wprowadzone = input("Podaj hasło: ")

if login_wprowadzony == LOGIN and haslo_wprowadzone == HASLO:
      print("Poprawnie zalogowano")
else:
      print("Niepoprawny login lub hasło")

print("===== Zadanie 3 =====")

'''
Stwórz program, który obsłuży proces dwuetapowego logowania. Użytkownik
zostanie poproszony o wprowadzenie czterocyfrowego PINu. Jeśli poda błędny
PIN, program wyświetli odpowiedni komunikat o błędzie. W przypadku poprawnego
PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

PIN: „1234”
Hasło: „Masło”

1. Użytkownik podaje PIN
2. Sprawdzamy czy użytkownik podał poprawny PIN
      -> Jeżeli tak, to użytkownik podaje hasło.
            -> Sprawdzamy czy użytkownik podał dobre hasło
                  -> Jeżeli tak, to poprawnie zalogowano
                  -> Jeżeli nie to wprowadzono niepoprawne hasło
      -> Jeżeli nie, to komunikat o tym że wprowadzono niepoprawny pin
'''

