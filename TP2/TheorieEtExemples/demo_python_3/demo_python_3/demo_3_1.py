# Programme 3-1
# Créé par Steve Godmaire 2026
# --
# Programme qui demande des nombres tant que l'utilisateur n'entre pas zéro.
# Stocker les nombres dans une liste et afficher les informations demandées.

# Importer les modules supplémentaires
import demo_3_fonctions as fct

# Déclarer les variables
entiers = []

# Boucle qui ajoute les nombres à la liste
while True:
    # Saisir un nombre
    entier = fct.lire_entier(
        "Entrez un nombre entier (0 pour arrêter) : ",
        "Nombre entier invalide, recommencez : ")

    # Si le nombre est zéro, on doit quitter
    if entier == 0:
        break

    # Ajouter le nombre à la liste
    entiers.append(entier)

# Afficher les résultats
print("\33[34m")
taille = len(entiers)

if taille == 0:
    print("Aucun nombre entré")
else:
    valeur_min = min(entiers)
    valeur_max = max(entiers)
    somme = sum(entiers)
    nombres_ordonnes = sorted(entiers)
    nombres_ordonnes_inverses = sorted(entiers, reverse=True)

    print(f"Taille : {taille}")
    print(f"Valeur minimale : {valeur_min}")
    print(f"Valeur maximale : {valeur_max}")
    print(f"Somme : {somme}")
    print(f"Ordre croissant : {nombres_ordonnes}")
    print(f"Ordre décroissant : {nombres_ordonnes_inverses}")
