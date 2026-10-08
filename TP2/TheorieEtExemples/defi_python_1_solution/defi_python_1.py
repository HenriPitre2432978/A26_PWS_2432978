# Défi Python #1
# Créé par Steve Godmaire 2026
# --
# Calculer la masse et la longueur d'une voiture en mouvement.

# Importer les modules externes
import math
import scipy.constants as cst

# Fonction qui calcule la masse d'un objet en mouvement
def calculer_masse_en_mouvement(masse, vitesse):
    m = masse / math.sqrt(1 - (vitesse**2 / cst.c**2))
    return m

# Fonction qui calcule la longueur d'un objet en mouvement
def calculer_longueur_en_mouvement(longueur, vitesse):
    l = longueur * math.sqrt(1 - (vitesse**2 / cst.c**2))
    return l

# Saisir les données initiales
print("Entrez les informations de la voiture :")
masse_au_repos = float(input("   Masse (en kg)        : "))
longueur_au_repos = float(input("   Longueur (en mètres) : "))
vitesse_kmh = float(input("   Vitesse (km/h)       : "))

# Récupérer la masse et longueur en mouvement
vitesse_ms = vitesse_kmh * 1000 / 3600  # Conversion de km/h à m/s
masse_en_mouvement = calculer_masse_en_mouvement(masse_au_repos, vitesse_ms)
longueur_en_mouvement = calculer_longueur_en_mouvement(longueur_au_repos, vitesse_ms)

# Afficher les résultats
print()
print(f"Une voiture qui roule à {vitesse_kmh} km/h", end=" ")
print(f"a une masse de {masse_en_mouvement} kg", end=" ")
print(f"et une longueur de {longueur_en_mouvement} mètres.")
