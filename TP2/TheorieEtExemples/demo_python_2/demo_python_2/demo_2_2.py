# Programme 2-2
# Créé par Steve Godmaire 2026
# --
# Demander une année et afficher si c'est une année bissextile.

# Saisir l'année à vérifier
annee = int(input("Quelle est l'année à tester? "))

# Calculer les tests : division par 4, 100 et 400
divisible_par_4 = annee % 4 == 0
divisible_par_100 = annee % 100 == 0
divisible_par_400 = annee % 400 == 0

# Est-ce une année bissextile?
if divisible_par_400:
    est_bissextile = True
elif divisible_par_100:
    est_bissextile = False
elif divisible_par_4:      
    est_bissextile = True
else:
    est_bissextile = False

# Afficher le résultat
print()
if est_bissextile:
    print(f"{annee} est une année bissextile.")
else:
    print(f"{annee} n'est pas une année bissextile.")
