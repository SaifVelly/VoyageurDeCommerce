import pandas as pd
from itertools import permutations

def trouver_plus_court_chemin(fichier_excel):
    # Lire le fichier Excel
    distances = pd.read_excel(fichier_excel, index_col=0)
    
    # Obtenir la liste des villes
    villes = distances.index.tolist()
    nb_villes = len(villes)
    
    # Initialiser la longueur minimale du chemin et le chemin correspondant
    longueur_minimale = float('inf')
    chemin_minimal = None
    
    # Générer toutes les permutations des villes
    permutations_villes = permutations(villes)
    
    # Parcourir toutes les permutations des villes
    for permutation in permutations_villes:
        longueur_chemin = 0
        for i in range(nb_villes - 1):
            longueur_chemin += distances.loc[permutation[i], permutation[i+1]]
        
        # Vérifier si ce chemin est plus court que le chemin minimal actuel
        if longueur_chemin < longueur_minimale:
            longueur_minimale = longueur_chemin
            chemin_minimal = permutation
    
    if chemin_minimal:
        print("Le chemin le plus court est :", chemin_minimal)
        print("La longueur du chemin le plus court est :", longueur_minimale)
    else:
        print("Il n'y a pas de chemin entre la ville 1 et la ville n.")

# Utilisation de la fonction en passant le nom du fichier Excel en tant qu'argument
trouver_plus_court_chemin("C:/Users/pc/Desktop/Classeur1.xlsx")
