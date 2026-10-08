# Programme 3-2
# Créé par Steve Godmaire 2026
# --
# Programme qui demande à l'utilisateur d'entrer les informations
# d'éléments du tableau périodique. L'utilisateur entrera préalablement
# le nombre d'éléments qu'il désire entrer.

# Importer les modules supplémentaires
import demo_3_fonctions as fct

# Fonction qui lit et retourne l'état d'un élément (gaz, liquide ou solide)
def lire_etat():
    etat = fct.lire_texte_non_vide(
        "État standard (gaz, liquide ou solide) : ",
        "État standard obligatoire, recommencez : ")
    
    while etat != "gaz" and etat != "liquide" and etat != "solide":
        etat = fct.lire_texte_non_vide(
            "État standard invalide, recommencez : ",
            "État standard obligatoire, recommencez : ")
        
    return etat

# Fonction qui lit et retourne un élément du tableau périodique (dictionnaire)
# Les informations sont demandées directement à l'utilisateur
def lire_element():
    element = {}
    
    element["nom"] = fct.lire_texte_non_vide(
        "Nom : ",
        "Nom obligatoire, recommencez : ")
    
    element["symbole"] = fct.lire_texte_non_vide(
        "Symbole chimique : ",
        "Symbole chimique obligatoire, recommencez : ")
    
    element["numero"] = fct.lire_entier_min_max(
        "Numéro atomique (1 à 118) : ",
        "Numéro atomique invalide, recommencez : ",
        1, 118)
    
    element["etat"] = lire_etat()
    
    return element

# Fonction qui affiche un élément
def afficher_element(element):
    print(f"   No   : {element['numero']}")
    print(f"   Nom  : {element['nom']} ({element['symbole']})")
    print(f"   État : {element['etat']}")

# Déclarer les variables
elements = []

# Saisir le nombre d'éléments à entrer
nb_elements = fct.lire_entier_superieur_zero(
        "Nombre d'éléments à lire : ",
        "Le nombre d'éléments doit être supérieur à zéro, recommencez : ",
        "Nombre d'éléments invalide, recommencez : ")

# Boucle qui ajoute les éléments à la liste
for i in range(1, nb_elements + 1):
    print(f"\nEntrez les informations de l'élément #{i}")
    element = lire_element()
    elements.append(element)

# Afficher les résultats
print("\33[32m")
print("*" * 40)
for i in range(nb_elements):
    print(f"Élément #{i+1} :")
    afficher_element(elements[i])
    print("*" * 40)
