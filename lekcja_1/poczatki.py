print("Cześć, jestem Python ;D")
print("A ty jak masz na imię?")
imie = input() # np. imie = Karol
print("Cześć", imie)
print(f"Cześć {imie}")

print("Ja powstałem w 1991 roku, dzięki pracy programisty Guido van Rossuma")
rok_urodzenia = input("A kiedy Ty się urodziłeś? ") # input zawsze zwraca typ 'str', czyli string 
wiek = 2025 - int(rok_urodzenia)
print(f"Wow masz już {wiek} lat!")