# Programme 3-3
# Créé par Steve Godmaire 2026
# --
# Programme qui demande à l'utilisateur 2 coordonnées (x1, y1) et (x2, y2),
# puis affiche le vecteur passant du premier au deuxième point.
# Utiliser les tuples pour stocker les coordonnées et le vecteur.

# Importer les modules supplémentaires
import demo_3_fonctions as fct

# Fonction qui calcule et retourne le vecteur passant
# du premier point au deuxième point.
def calculer_vecteur(point1, point2):
    # Calculer les composantes du vecteur
    vecteur_x = point2[0] - point1[0]
    vecteur_y = point2[1] - point1[1]

    # Retourner le vecteur
    return (vecteur_x, vecteur_y)

# Saisir les coordonnées du premier point
print("Entrez les coordonnées du premier point :")
x1 = fct.lire_entier("  x : ", "  x invalide, recommencez : ")
y1 = fct.lire_entier("  y : ", "  y invalide, recommencez : ")

# Saisir les coordonnées du deuxième point
print("\nEntrez les coordonnées du deuxième point :")
x2 = fct.lire_entier("  x : ", "  x invalide, recommencez : ")
y2 = fct.lire_entier("  y : ", "  y invalide, recommencez : ")

# Créer les tuples pour les deux points
point1 = (x1, y1)
point2 = (x2, y2)

# Calculer le vecteur
vecteur = calculer_vecteur(point1, point2)

# Afficher les paramètres du vecteur
print("\33[34m")
print("*" * 55)
print(f"Le vecteur qui passe de {point1} à {point2} est : {vecteur}")
print("*" * 55)
