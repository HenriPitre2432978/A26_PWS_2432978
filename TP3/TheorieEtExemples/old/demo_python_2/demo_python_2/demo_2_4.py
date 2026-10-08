# Programme 2-4
# Créé par Steve Godmaire 2026
# --
# Écrire un programme pour tester si un nombre entier "n" est premier.

# Importer les modules supplémentaires
import math

# Fonction qui vérifie si un nombre entier est premier
def est_premier(entier):
    # Un nombre n'est pas premier s'il est égal ou plus petit que 1
    if entier <= 1:
        return False
    
    # Calculer la racine du nombre arrondi vers le bas
    racine = int(math.sqrt(entier))
    
    # Boucle qui retourne faux s'il existe un diviseur
    for i in range(2, racine + 1):
        if entier % i == 0:
            return False
    
    # Si on se rend ici, l'entier est un nombre premier
    return True

# Saisir un entier
entier = int(input("Entrez un nombre entier : "))

# Afficher le résultat
print()
if est_premier(entier):
    print(f"{entier} est un nombre premier.")
else:
    print(f"{entier} n'est pas un nombre premier.")
