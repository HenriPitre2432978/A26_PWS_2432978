# Programme 1-6
# Créé par Steve Godmaire 2026
# --
# Calculer les montants des taxes et le montant total d'un article.

# Déclaration des constantes
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

# Fonction qui calcule les taxes et le total
def calculer_taxes_et_total(prix):
    # Calculer les taxes et le total
    tps = prix * TAUX_TPS
    tvq = prix * TAUX_TVQ
    total = prix + tps + tvq
    
    # Retourner les taxes et le total
    return tps, tvq, total

# Saisir le prix de l'article
prix = float(input("Quel est le prix de l'article ? "))

# Récupérer les taxes et le total
tps, tvq, total = calculer_taxes_et_total(prix)

# Afficher les résultats
print()
print(f"Prix de l'article : {prix:9.2f}$")
print(f"TPS ({TAUX_TPS:.0%})          : {tps:9.2f}$")
print(f"TVQ ({TAUX_TVQ:.3%})      : {tvq:9.2f}$")
print("-"*30)
print(f"TOTAL             : {total:9.2f}$")
