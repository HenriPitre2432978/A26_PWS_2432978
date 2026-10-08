# Programme 1-5
# Créé par Steve Godmaire 2026
# --
# Calculer la longueur de l'hypoténuse d'un triangle rectangle.

# Saisir les longueurs des côtés a et b
cote_a = int(input("La longueur du côté \"a\" : "))
cote_b = int(input("La longueur du côté \"b\" : "))

# Récupérer la longueur de l'hypoténuse
hypotenuse = (cote_a**2 + cote_b**2)**0.5

# Afficher le résultat
print()
print("L'hypoténuse d'un triangle rectangle de côtés", end=" ")
print(f"{cote_a} et {cote_b} mesure {hypotenuse}")
