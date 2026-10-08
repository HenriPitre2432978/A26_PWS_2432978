# Programme 3-Fonctions
# Créé par Steve Godmaire 2026
# --
# Fonctions communes aux différents programmes.

# Fonction qui lit et retourne un nombre entier valide
def lire_entier(message, message_invalide):
  reponse = input(message)
  while True:
    try:
      entier = int(reponse)
      return entier
    except ValueError:
      reponse = input(message_invalide)

# Fonction qui lit et retourne un entier valide supérieur à zéro
def lire_entier_superieur_zero(message, message_inferieur, message_invalide):
  reponse = input(message)
  while True:
    try:
      entier = int(reponse)

      if entier <= 0:
        reponse = input(message_inferieur)
        continue
    
      return entier
    except ValueError:
      reponse = input(message_invalide)

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

# Fonction qui lit et retourne un texte non vide
def lire_texte_non_vide(message, message_invalide):
    reponse = input(message).strip()
    while reponse == "":
        reponse = input(message_invalide).strip()
    return reponse
