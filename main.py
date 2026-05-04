# main.py

import os
from media import Film, Serie
from mediatheque import Mediatheque

# Chemins des fichiers
CHEMIN_JSON = os.path.join("data", "mediatheque.json")
CHEMIN_CSV  = os.path.join("exports", "catalogue.csv")
CHEMIN_TXT  = os.path.join("exports", "rapport.txt")

# Création des dossiers si inexistants
os.makedirs("data", exist_ok=True)
os.makedirs("exports", exist_ok=True)

# --- Initialisation ---
m = Mediatheque()

# --- Chargement des données existantes ---
m.charger_json(CHEMIN_JSON)

# --- Ajout de médias ---
# TODO: créer et ajouter au moins 3 films et 2 séries avec des statuts variés
#       ("à voir", "en cours", "vu")


# --- Affichage de tous les médias ---
print("=== Tous les médias ===")
# TODO: appeler la méthode afficher_tout()


# --- Recherche d'un média ---
print("\n=== Recherche ===")
# TODO: rechercher un média par titre et afficher le résultat


# --- Suppression d'un média ---
print("\n=== Suppression ===")
# TODO: supprimer un média par titre
# TODO: afficher la liste après suppression


# --- Sauvegarde JSON ---
# TODO: sauvegarder la médiathèque dans le fichier JSON


# --- Export CSV ---
# TODO: exporter la médiathèque en CSV


# --- Génération du rapport TXT ---
# TODO: générer le rapport textuel