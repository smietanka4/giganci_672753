'''
1) Choinka / Piramida
      Napisz program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie
      wyświetli choinkę / piramidę o podanej wysokości. Choinka ma składać się z gwiazdek
      '*' oraz spacji jako znaków białych.

      *
     * *
    * * *
   * * * *

      *
     ***
    *****
   *******


2) Prostokąt
      Napisz program, który wczyta od użytkownika dwie liczby: wysokość i szerokość, a
      następnie wypisze w konsoli prostokąt składający się z gwiazdek.
      Przygotuj dwie wersje programu: prostokąt pusty w środku i wypełniony. Zapytaj
      użytkownika, którą wersję chciałby zobaczyć lub wyświetl obie jeden po drugim.

3) Sekwencja Fibonacciego
      Napisz program, który zapyta użytkownika o liczbę dodatnią (sprawdzi jej poprawność)
      a następnie wypisze podaną liczbę elementów ciągu Fibonacciego w konsoli.
      Dodatkowe: Program, który wypisze wszystkie elementy ciągu Fibonacciego, które są
      mniejsze od wprowadzonej liczby.
'''

print("===== Zadanie 1 =====")

wysokosc = int(input("Podaj wysokość choinki: "))

for i in range(1, wysokosc + 1):
    print(" " * (wysokosc - i) + "* " * i)

print("\nPiramida:")
for i in range(1, wysokosc + 1):
    print(" " * (wysokosc - i) + "*" * (2 * i - 1))


print("===== Zadanie 2 =====")

wysokosc = int(input("Podaj wysokość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))

print("\nProstokąt wypełniony:")
for i in range(wysokosc):
    print("*" * szerokosc)

print("\nProstokąt pusty w środku:")
for i in range(wysokosc):
    if i == 0 or i == wysokosc - 1:
        print("*" * szerokosc)
    else:
        print("*" + " " * (szerokosc - 2) + "*")


print("===== Zadanie 3 =====")

n = int(input("Podaj liczbę dodatnią: "))

if n <= 0:
      print("Podaj liczbę dodatnią!")
else:
      print("Pierwsze", n, "elementów ciągu Fibonacciego:")
      a, b = 0, 1
      for i in range(n):
            print(a)
            a, b = b, a + b

      print("Elementy mniejsze od",n,":")
      a, b = 0, 1
      while a < n:
            print(a)
            a, b = b, a + b

