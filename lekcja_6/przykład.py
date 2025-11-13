# Przykład prostego warunku (tworzymy zmienną warunek, która jest naszym sędzią)

wprowadzone_hasło = input("Podaj hasło: ")

poprawnosc_hasla = ("Maslo" == wprowadzone_hasło)

if poprawnosc_hasla:
      print(True)
else:
      print(False)

# Przykład złożonego warunku. Nawiasy mają kolejność w sprawdzaniu warunków

a = 10
b = 12
c = -5

if a == 20 and (b > 10 or c >= -5):
      print("Warunek prawdziwy")

# Słowo kluczowe 'in'
print("konstrukcja substring in string")
# podciąg znaków w ciągu znaków

napis = "Karol"

if "arl" in napis:
      print("arl znajduje sie w napisie")
elif "K" in napis:
      print("K znajduje sie w napisie")

print("=== Przykład dlaczego if działa tak a nie inaczej ===")

pin = "123"
haslo = "456"

pin_s = input("podaj pin: ")
haslo_s = input("podaj hasło: ")

if pin_s and haslo_s == pin and haslo:
      print("poprawnie")


print("=== ZAGNIEŻDŻONE INSTRUKCJE WARUNKOWE ===")

warunek1 = True
warunek2 = False
warunek3 = True
warunek4 = True

if warunek1: 
      # Jeśli warunek1 prawdziwy, to przechodzimy do instrukcji niżej
      if warunek2: 
            # Kod wykona się jeśli warunek1 i warunek2 są prawdziwe
            pass
      elif warunek3:
            # Kod wykona się jeśli warunek1 był prawdziwy, warunek2 był fałszywy, warunek3 był prawdziwy
            pass
      else:
            # Kod wykona się jeśli warunek1 był prawdziwy, i żaden z powyższych nie był prawdziwy
            pass
elif warunek4:
      # Kod wykona się jeśli warunek1 nie był prawdziwy, a warunek4 był prawdziwy
      pass
else:
      # Kod wykona się jeśli ani warunek1 ani warunek4 nie był prawdziwy
      pass








