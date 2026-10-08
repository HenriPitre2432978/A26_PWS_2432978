# Programme 1-5 (alt)
# Créé par Steve Godmaire 2026
# --
# Calculer la longueur de l'hypoténuse d'un triangle rectangle.

# Fonction qui calcule l'hypoténuse d'un triangle rectangle
def calculer_hypotenuse(cote_a, cote_b):
    # Calculer l'hypoténuse
    hypotenuse = (cote_a**2 + cote_b**2)**0.5
    
    # Retourner l'hypoténuse
    return hypotenuse

# Saisir les longueurs des côtés a et b
cote_a = int(input("La longueur du côté \"a\" : "))
cote_b = int(input("La longueur du côté \"b\" : "))

# Récupérer la longueur de l'hypoténuse
hypotenuse = calculer_hypotenuse(cote_a, cote_b)

# Afficher le résultat
print()
print("L'hypoténuse d'un triangle rectangle de côtés", end=" ")
print(f"{cote_a} et {cote_b} mesure {hypotenuse}")
