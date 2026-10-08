# Défi Python #3
# Créé par Steve Godmaire 2026
# --
# Programme qui demande à l'utilisateur d'entrer à la console des noms
# d'animaux et qui affiche à la fin la liste en ordre alphabétique.

# Déclarer les variables
animaux = []  # liste vide

# Saisir les animaux
print("Entrez des noms d'animaux (appuyez sur Entrée pour terminer) :")
while True:
    # strip permet d'enlever les espaces au début et à la fin
    animal = input(f"  #{len(animaux) + 1} : ").strip()
    
    # Si le nom fourni est vide, on sort de la boucle
    if animal == "":
        break
    
    # Ajouter à la liste
    animaux.append(animal)

# Trier les animaux en ordre alphabétique
animaux.sort()

# Afficher les résultats
print()
print("*" * 30)
if len(animaux) == 0:
    print("Aucun animal entré")
else:
    print("Animaux triés en ordre alphabétique :")
    for animal in animaux:
        print(f"  {animal}")
print("*" * 30)
