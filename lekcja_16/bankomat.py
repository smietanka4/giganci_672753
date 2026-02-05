'''
Przygotujmy funkcję, która będzie miała za zadanie wyświetlać menu naszego bankomatu.
'''
def menu():
     print("Wybierz opcje: ")
     print("1. Wpłata") 
     print("2. Wypłata")
     print("3. Sprawdzenie stanu konta")
     print("4. Zakończ")

def pokaz_stan_konta(saldo):
      print(f"Stan konta wynosi {saldo} złotych")

'''
Przygotujmy funkcję odpowiedzialną za wpłatę na konto, która zwróci nowe saldo po wpłacie
-> pobrać od użytkownika ilość wpłacanej gotówki
-> dodać gotówkę do salda na koncie
-> wyświetlić stan konta po transakcji
'''

def wplata(saldo):
      kwota_wplaty = int(input("Ile chcesz wpłacić?: "))
      saldo += kwota_wplaty
      pokaz_stan_konta(saldo)
      return saldo

'''
Przygotujmy funkcję odpowiedzialną za wypłatę pieniędzy z konta, która również zwróci nowe saldo po wypłacie.
-> pobrać od użytkownika ilość wypłacanej gotówki
-> sprawdzić czy użytkownik nie próbuje wypłacić więcej niż ma na koncie
      -> Jeśli TAK, to wyświetlamy odpowiedni komunikat i zwracany saldo konta
      -> Jeśli NIE, to odejmujemy gotówkę z konta i wyświetlamy odpowiedni komunikat
-> wyświetlić stan konta
'''

def wyplata(saldo):
      kwota_wyplaty = int(input("Podaj ile chcesz wypłacić?: ")) 
      if kwota_wyplaty > saldo:
            print("Operacja nie udana, za mało środków na koncie")
            return saldo
      else:
            saldo -= kwota_wyplaty
            print(f"Wypłacono {kwota_wyplaty} złotych")
            pokaz_stan_konta(saldo)
            return saldo

# powyżej tych zmiennych będziemy pisać wszystkie funkcje naszego programu
saldo = 0
wybor = 0

# poniżej będzie główną pętla programu
while wybor != 4:
      menu()
      wybor = int(input("Twój wybór to: "))
      if wybor == 1:
            saldo = wplata(saldo)
      elif wybor == 2:
            saldo = wyplata(saldo)
      elif wybor == 3:
            pokaz_stan_konta(saldo)
      elif wybor == 4:
            print("Wyłączanie bankomatu.")
      else:
            print("Niepoprawny wybór")
