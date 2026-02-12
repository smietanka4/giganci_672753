# BAZA DANYCH

zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "jeten"]
dwa = ["2", "dwa", "dwójkę", "dwójka"]
trzy = ["3", "trzy", "trójkę", "trójka"]
cztery = ["4", "cztery", "czwórkę", "czwórka"]
piec = ["5", "pięć", "piątkę", "piątka"]
szesc = ["6", "sześć", "szóstkę", "szóstka"]
siedem = ["7", "siedem", "siódemkę", "siódemka"]
osiem = ["8", "osiem", "ósemkę", "ósemka"]
dziewiec = ["9", "dziewięć", "dziewiątkę", "dziewiątka"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dychę"]
jedenascie = ["11","jedenaście", "jedenastkę", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastu", "dwunastkę"]
trzynascie = ["13", "trzynaście","trzynastu","trzynastkę"]
czternascie = ["14", "czternaście", "czternastu", "czternastkę"]
pietnascie = ["15", "piętnaście","piętnastu", "piętnastkę"]
szesnascie = ["16", "szesnaście","szesnastu","szesnastkę"]
siedemnascie = ["17","siedemnaście", "siedemnastu", "siedemnastkę"]
osiemnasice = ["18", "osiemnaście","osiemnastu","osiemnastkę"]
dziewietnascie = ["19","dziewiętnaście", "dziewiętnastu","dziewiętnastkę"]
plus = ["+", "dodaj", "plus", "dodać", "dodawanie", "dodac"]
minus = ["-", "odejmij", "minus", "odjąć"]
gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
ukosnik = ["/", ":", "dzielone", "podziel"]

baza = [zero, jeden,dwa,trzy, cztery, piec, szesc,siedem, osiem, dziewiec,
      dziesiec,jedenascie,dwanascie,trzynascie,czternascie,pietnascie,szesnascie,siedemnascie,osiemnasice,dziewietnascie, 
      plus, minus, gwiazdka, ukosnik]
 

# FUNKCJE

def przetlumacz(slowo):
      for baza_symbolu in baza:
            for slowo_bazy_symbolu in baza_symbolu:
                  if slowo == slowo_bazy_symbolu:
                        return baza_symbolu[0] # zwracamy pierwszy element listy w której znaleźliśmy pasujące słowo
      return "" # jeśli słowo, które próbujemy przetłumaczyć na liczbę lub operator nie występuje w naszych tablicach to je pomijamy

# np.: tekst = "0+1"
def oblicz_z_tekstu(tekst):
      wynik = 0
      liczba = ""
      operacja = ""

      for znak in tekst:
            if znak.isdigit(): # metoda .isdigit() sprawdza czy podany objekt jest cyfrą, jeżeli tak to zwraca True, jeśli nie to zwraca False
                  liczba += znak
            elif liczba:
                  if operacja == "":
                        wynik = int(liczba)
                  else:
                        wynik = oblicz(wynik, int(liczba), operacja)
                  operacja = znak
                  liczba = ""
      if liczba:
            wynik = oblicz(wynik, int(liczba), operacja)
      return wynik

def oblicz(liczba1, liczba2, operacja):
      if operacja == "+":
            return liczba1 + liczba2
      elif operacja == "-":
            return liczba1 - liczba2
      elif operacja == '*':
            return liczba1 * liczba2
      elif operacja == '/':
            return liczba1 / liczba2
      # dalej robimy to samo z innymi znakami operacji arytmetycznych


dzialanie = ""
tekst = input("Podaj tekst: ")

for slowo in tekst.split(" "): # .split(separator) to metoda, która służy do dzielenia ciągu znaków (stringa) na mniejsze części na podstawie podanego przez nas separatora (np. spacji czy przecinka), .split() zwraca listę stringów
      slowo = slowo.lower() # .lower() to metoda, używana na ciągach znaków, która konwertuje cały tekst na małe litery
      dzialanie += przetlumacz(slowo)

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))