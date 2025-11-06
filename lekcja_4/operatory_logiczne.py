# Operatory relacyjne

print("=== Operatory relacyjne ===")
print(250 > 67) # Większe, Prawda
print(67 >= 68) # Większe bądź równe, Fałsz
print(24 == 12) # 24 jest równe 12, Fałsz
print(67 != 60) # 67 jest różne od 60, Prawda
print(250 < 67) # Mniejsze, Fałsz
print(67 <= 68) # Mniejsze bądź równe, Fałsz

# Zadanie 1
print("=== Zadanie 1 ===")

print(12 == 15) # Fałsz # ==, <, !=, <=
print(5 <= 15000) # Prawda # ==, >, >=, <=
print(120 != 120) # Fałsz # ==, >=, !=, <=
print(60 == 15) # Fałsz # ==, <, !=, >=
print(25.3421 == 25.3421) # Prawda # ==, <, !=, <=
print(99 <= 98.5) # Fałsz # ==, >=, !=, <=
print(40.10 < 40.12) # Prawda # ==, <, !=, <= 

# Zadanie 2 - rollercoaster

'''
Program pytający użytkownika o jego wzrost, aby na tej podstawie określić czy
może skorzystać z rollercoastera.

Pytania pomocnicze:
W jaki sposób sformułujemy zdanie opisujące werdykt pozytywny?
Jaki musi być wzrost, aby wynik był prawdą?

Kryterium:

Wzrost osoby, wyrażony w centymetrach, musi być większy niż 150.

input() -> Pozwala wprowadzić użytkownikowi coś z klawiatury (Pyta użytkownika o coś)
print() -> Drukuje napis na konsole
int() -> Konwertuje argument na typ 'int'
'''

print("Czy możesz korzystać z roller-coastera?")

wzrost = int(input("Podaj wzrost w cm: ")) # input() zawsze zwraca typ string

werdykt = wzrost > 150
print(werdykt)

# Działania Logiczne

# Operator jednoargumentowy NOT
print("=== Operator NOT ===")

print(not True) # False
print(not False) # True

#przykłady
print("=== Przykłady dla operatora NOT ===")
print('not 50 == 51: ',not 50 == 51) # not False -> True
print('not (not 4 > 10): ', not (not 4 > 10)) # not (not 4 > 10) -> not (not False) -> not True -> False 

# Operator dwuargumentowy AND
print("=== Operator AND ===")

print('True and True => ', True and True)
print('True and False => ', True and False)
print('False and True => ', False and True)
print('False and False => ', False and False)

#przykłady
print("=== Przykłady do operatora AND ===")

print('20 < 25 and 24 == 0 => ', 20 < 25 and 24 == 0) # True and False => False
print('True and True and False and True =>', True and True and False and True)

# Operator dwuargumentowy OR
print("=== Operator OR ===")
print('True or True => ', True or True)
print('True or False => ', True or False)
print('False or True => ', False or True)
print('False or False => ', False or False)

#przykłady
print("=== Przykłady do operatora OR ===")

print('20 < 25 or 24 == 0 => ', 20 < 25 or 24 == 0) # True or False => True 

print("===== ZADANIE 3 =====")

'''
Program pytający użytkownika o jego wzrost, aby na tej podstawie określić czy
może skorzystać z rollercoastera.

Pytania pomocnicze:
W jaki sposób sformułujemy zdanie opisujące werdykt pozytywny?
Jaki musi być wzrost, aby wynik był prawdą?

Kryterium:

Wzrost osoby, wyrażony w centymetrach, musi być większy niż 150 i jednocześnie mniejszy niż 215.

input() -> Pozwala wprowadzić użytkownikowi coś z klawiatury (Pyta użytkownika o coś)
print() -> Drukuje napis na konsole
int() -> Konwertuje argument na typ 'int'
'''

print("Czy możesz korzystać z roller-coastera?")

wzrost = int(input("Podaj wzrost w cm: ")) # input() zawsze zwraca typ string

werdykt = wzrost > 150 and wzrost < 215
print(werdykt)

print("======= Zadanie Teoretyczne =======")
# Wstawiamy operatory logiczne: AND, OR lub NOT

print(True, (25 < 140) and (10 == 10)) # True and True => True
print(True, 100 >= 1 or 2 > 10) # True or False => True 
print(False, 25 < 14 or 10 != 10) # False or False => False
print(False, (-1 < 3) and (2 < 9) and (10 == 15)) # (True and True) and False => True and False => False
print(True, (20.05 < 21 < 10) or (-10 < 20 < 150 <= 150)) # False or True => True
print(False, (1 < 10) and (2 < 15) and (-50 == 42)) # (True and True) and False => True and False => False 
print(True, not 2 == 10) # => not False => True




















