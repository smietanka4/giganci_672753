# # Pętla while - pętla "dopóki"

# warunek = True

# while warunek: # dopóki warunek jest prawdziwy, pętla się wykonuje
#       # Kod, który może być powtarzany
#       pass

# # Zastosowania pętli
# '''
# 1. Nie musimy powtarzać kodu
# 2. Kod jest czysty i przejrzysty i krótszy
# '''

# i = 0             # Ustawiamy zmienna pomocniczą (iterator) na 0
# while i < 25: # Dopóki zmienna "i" jest mniejsza od 25 to wykonuj
#       print("Hej Gigancie") # w każdym wykonaniu pętli drukujemy napis
#       i += 1 # Dodajemy do zmiennej "i" + 1, żeby pętla się kiedyś zatrzymała

# # Moduł time pozwala nam np. na manipulowanie czasem wykonania zadań w konsoli
import time

# print("Start")
# time.sleep(5) # "Usypiamy konsole na 5 sekund"
# print("Koniec")

# # Moduł random pozwala nam na losowanie liczb
# import random

# liczba = random.randint(1, 10)
# print(liczba)


# Pętla nieskończona
# while True: 
#       print("You can't stop me now!")
#       time.sleep(1)
#       # break - przerywa działanie pętli
#       break
# print("Ha! - I am a programmer so I can")

# przykład działania continue
# continue - gdy napotkane pomija jedno wykonanie pętli, ale pętla dalej sie wykonuje
PIN = "1234"
ROK_URODZENIA = "1998"
HASLO = "qwerty"

while True:
      input_pin = input("PIN: ")
      if input_pin != PIN:
            print("Odmowa dostępu!")
            continue

      input_rok_urodzenia = input("Rok urodzenia: ")
      if input_rok_urodzenia != ROK_URODZENIA:
            print("Odmowa dostępu! Zaloguj się ponownie")
            continue

      input_haslo = input("Hasło: ")
      if input_haslo != HASLO:
            print("Odmowa dostępu! Zaloguj się ponownie")
            continue
      
      print("Zalogowano poprawnie!")
      break

print("Super tajne treści znajdują się tutaj")


