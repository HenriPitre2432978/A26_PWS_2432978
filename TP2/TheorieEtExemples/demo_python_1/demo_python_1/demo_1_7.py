# Programme 1-7
# Créé par Steve Godmaire 2026
# --
# Calculer le nombre de molécules d'un composé chimique
# à l'aide de la constante d'Avogadro.

# Importer les modules supplémentaires
import scipy.constants as cst

# Fonction qui calcule le nombre de molécules
def calculer_nombre_molecules(nb_moles):
    # Calculer le nombre de molécules
    nb_molecules = nb_moles * cst.Avogadro
    
    # Retourner le nombre de molécules
    return nb_molecules

# Saisir les données initiales
nb_moles = float(input("Entrez le nombre de moles : "))

# Récupérer le nombre de moles et molécules
nb_molecules = calculer_nombre_molecules(nb_moles)

# Afficher les résultats
print()
print(f"Il y a {nb_molecules:.5} molécules dans {nb_moles} moles.")
