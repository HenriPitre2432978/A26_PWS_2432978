# Défi Python #2
# Créé par Steve Godmaire 2026
# --
# Programme dans lequel il faut deviner un nombre entier.
# Ce nombre (entre 1 et 20) est initialement choisi au hasard,
# et le joueur doit tenter de le trouver. 

# Importer les modules supplémentaires
import random
import Defi_2_fonctions as fct

# Déclarer les constantes
ENTIER_MIN = 1
ENTIER_MAX = 20

# Déclarer les variables
nb_tentatives = 0

# Tirer l'entier secret
entier_secret = random.randint(ENTIER_MIN, ENTIER_MAX)

# Faire deviner, tant que la réponse est mauvaise
while True:
    # Saisir le choix de l'utilisateur
    choix = fct.lire_entier_min_max(
        f"Quel est le nombre ({ENTIER_MIN} à {ENTIER_MAX})? ",
        "Entier invalide, recommencez : ",
        ENTIER_MIN, ENTIER_MAX)
    
    # Incrémenter le nombre de tentatives
    nb_tentatives += 1

    # Valider le choix
    if choix == entier_secret:
        break # Le choix est bon --> on quitte la boucle
    elif choix < entier_secret:
        print("Le nombre est plus haut.")
    else:
        print("Le nombre est plus petit")

# Afficher le message final
print()
print("*" * 40)
print("Bravo!")
print(f"La bonne réponse était {entier_secret}.")
print(f"Vous avez trouvé en {nb_tentatives} tentatives.")
print("*" * 40)
