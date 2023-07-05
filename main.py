"""
    @author: Kevin
"""

# importation des bibliotheques
import pandas as pd

# 1- Lecture du fichier csv et stockage dans une structure de données appropriée
csv_path = "Data.csv"
ventes_df = pd.read_csv(csv_path, encoding="utf-8", sep=",")

print(ventes_df)

# 2- Calcul des ventes totales et le bénéfice pour chaque région
# Traitement de données
# Ajout des colonnes cout_reel et benefice

ventes_df["cout_reel"] = ventes_df["quantite_vendue"] * ventes_df["prix_unitaire"]

"""
    La colonne benefice désigne les benefices annexes liés à l'achat du produit
    Ces benefices sont à la charge du client
"""
ventes_df["benefice"] = ventes_df["cout_total"] - ventes_df["cout_reel"]

print(ventes_df)

# Calcul des ventes totales pour chaque région
vente_totale_par_region = ventes_df.groupby("region")[ "cout_total"].sum()
# vente_totale_par_region = ventes_df.groupby("region").agg(ventes_totales_par_region = ("cout_total", "sum"))

print(vente_totale_par_region)

# Calcul du bénéfice pour chaque région
benefice_par_region = ventes_df.groupby("region").agg(benefices = ("benefice", "sum"))

print(benefice_par_region)

# 3- Pourcentage de ventes totales de chaque produit pour l'ensemble de l'entreprise
# Ventes totales: Somme des ventes totales par region
ventes_totales = vente_totale_par_region['Nord'] + vente_totale_par_region['Sud']
# Vente par produit

# Je fais un groupby sur les produits en sommant le coût total
vente_produit = ventes_df.groupby("produit")["cout_total"].sum()
# Je transforme vente_produit en dataframe
vente_produit = pd.DataFrame(vente_produit)
vente_produit["pourcentage"] = vente_produit['cout_total'] / ventes_totales * 100
vente_produit["pourcentage"] = vente_produit["pourcentage"].apply(lambda x : f'{round(x)} %')
print(vente_produit)

##### BONUS ######

# Ajout de la fonctionnalité pour afficher les régions avec la plus grande marge bénéficiaire

# Je transforme mes séries en dataframa
vente_totale_par_region = pd.DataFrame(vente_totale_par_region)
benefice_par_region = pd.DataFrame(benefice_par_region)

# Je concatene mes 2 dataframes
marge_benefice_region = pd.concat([vente_totale_par_region, benefice_par_region], axis=1)
print(marge_benefice_region)
marge_benefice_region["marge_beneficiaire"] = (marge_benefice_region["benefices"] / marge_benefice_region["cout_total"]) * 100
marge_benefice_region["marge_beneficiaire"] = marge_benefice_region["marge_beneficiaire"].apply(lambda x : f'{round(x, ndigits=2)} %')
print(marge_benefice_region)

# Ajout de la fonctionnalité pour afficher les dates avec les ventes les plus élevées pour chaque région

# date_vente_produit_region = ventes_df.groupby(["region", "produit"])["cout_total"].sum()
# date_vente_produit_region = ventes_df.groupby(["region", "count_total"]).count_total.min()
date_vente_produit_region = ventes_df.groupby(["region", "date"])

# Je groupe les données par région et date en utilisant la méthode groupby() 
# et en calculant la somme du coût total pour chaque groupe en utilisant sum()
# Après, j'utilise sort_values('cout_total', ascending=False) pour trier le DataFrame
# groupé en fonction du coût total dans l'ordre décroissant.
grouped = ventes_df.groupby(["region", "date"])['cout_total'].sum().reset_index()
date_region_ventes_elevee = grouped.sort_values('cout_total', ascending=False)
print(date_region_ventes_elevee)
