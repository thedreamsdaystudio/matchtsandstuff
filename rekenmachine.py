# Definieer functie voor optellen
def optellen(a, b):
    return a + b

# Definieer functie voor aftrekken
def aftrekken(a, b):
    return a - b

# Definieer functie voor vermenigvuldigen
def vermenigvuldigen(a, b):
    return a * b

# Definieer functie voor delen
def delen(a, b):
    if b == 0:
        return "Kan niet delen door nul!"
    else:
        return a / b

print("Kies een bewerking:")
print("1. Optellen")
print("2. Aftrekken")
print("3. Vermenigvuldigen")
print("4. Delen")

# Vraag de gebruiker om een keuze te maken
keuze = input("Voer uw keuze in (1/2/3/4): ")

# Vraag de gebruiker om twee getallen in te voeren
getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))

if keuze == '1':
    print("Resultaat:", optellen(getal1, getal2))
elif keuze == '2':
    print("Resultaat:", aftrekken(getal1, getal2))
elif keuze == '3':
    print("Resultaat:", vermenigvuldigen(getal1, getal2))
elif keuze == '4':
    print("Resultaat:", delen(getal1, getal2))
else:
    print("Ongeldige invoer")
