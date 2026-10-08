# Programme 1-4
# Créé par Steve Godmaire 2026
# --
# Calculer le montant total d’une facture à partir du montant avant taxes.

# Déclarer les constantes et variables
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975
prix = 12.9

# Calculer les taxes et le montant total
tps = prix * TAUX_TPS
tvq = prix * TAUX_TVQ
total = prix + tps + tvq

# Afficher les résultats
print(f"Montant de la facture : {prix} $")

