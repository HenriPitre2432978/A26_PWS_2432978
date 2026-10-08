# Programme 1-4 (alt)
# Créé par Steve Godmaire 2026
# --
# Calculer le montant total d’une facture à partir du montant avant taxes.

# Déclarer les constantes
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

# Saisir le prix
prix = float(input("Montant de la facture : "))

# Calculer les taxes et le montant total
tps = prix * TAUX_TPS
tvq = prix * TAUX_TVQ
total = prix + tps + tvq

# Afficher les résultats
print()
print(f"Montant de la facture : {prix:9.5f} $")
print(f"Montant TPS           : {tps:9.5f} $")
print(f"Montant TVQ           : {tvq:9.5f} $")
print(f"-" * 35)
print(f"Montant total         : {total:9.5f} $")
