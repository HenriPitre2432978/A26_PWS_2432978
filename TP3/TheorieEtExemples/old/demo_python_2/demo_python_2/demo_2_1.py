# Programme 2-1
# Créé par Steve Godmaire 2026
# --
# Vérifier si une personne est majeure ou mineure (18 ans et +).

# Saisir l'âge de la personne
age = int(input("Quel âge avez-vous? "))

# Afficher le résultat
print()
if age >= 18:
  print(f"À {age} ans, vous êtes majeur.")
else:
  print(f"À {age} ans, vous êtes mineur.")
