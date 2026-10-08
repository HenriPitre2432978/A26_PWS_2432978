# Programme 2-5
# Créé par Steve Godmaire 2026
# --
# Écrire un programme qui tire aléatoirement une pièce de monnaie
# (pile ou face) un certain nombre de fois.

# Importer les modules supplémentaires
import random

# Déclarer les constantes
PILE = 0
FACE = 1

# Déclarer les variables
nb_piles = nb_faces = 0

# Saisir le nombre de tirs à faire
nb_tirs = int(input("Nombre de tirs à effectuer : "))

# Simuler les "n" tirs
for i in range(nb_tirs):
    tir = random.randint(0, 1)
    if tir == PILE:
        nb_piles += 1
    else:
        nb_faces += 1

# Calculer les pourcentages
pct_piles = nb_piles / nb_tirs
pct_faces = nb_faces / nb_tirs

# Afficher les résutlats
print()
print(f"Nombre de PILE : {nb_piles} ({pct_piles:.4%})")
print(f"Nombre de FACE : {nb_faces} ({pct_faces:.4%})")
