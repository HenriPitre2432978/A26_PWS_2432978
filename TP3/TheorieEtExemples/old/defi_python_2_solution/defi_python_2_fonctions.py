# Defi #2 - Fonctions
# Créé par Steve Godmaire 2025
# --
# Fonctions communes aux différents programmes.

# Fonction qui lit et retourne un nombre balisé valide
def lire_entier_min_max(message, message_invalide, min, max):
    reponse = input(message)
    while True:
        try:
            entier = int(reponse)

            if entier < min or entier > max:
                reponse = input(message_invalide)
                continue

            return entier
        except ValueError:
            reponse = input(message_invalide)
