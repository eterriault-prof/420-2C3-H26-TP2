# mediatheque.py

import json
import csv
import os
from media import Film, Serie


class Mediatheque:
    """Gère la collection de médias et les opérations sur les fichiers."""

    def __init__(self):
        # TODO: initialiser l'attribut liste comme une liste vide
        pass

    def ajouter(self, media):
        # TODO: ajouter l'objet media à self.liste
        pass

    def supprimer(self, titre):
        # TODO: parcourir self.liste et supprimer le média dont le titre
        #       correspond exactement au paramètre titre
        # TODO: si aucun média ne correspond, afficher un message d'erreur
        pass

    def rechercher(self, titre):
        # TODO: parcourir self.liste et retourner le premier média
        #       dont le titre correspond au paramètre titre
        # TODO: retourner None si aucun résultat
        pass

    def afficher_tout(self):
        # TODO: afficher tous les médias de self.liste
        #       en utilisant leur __str__ (via print)
        pass

    def charger_json(self, chemin):
        # TODO: si le fichier n'existe pas, ne rien faire (self.liste reste vide)
        # TODO: lire le fichier JSON et reconstruire les objets Film ou Serie
        #       selon la valeur de la clé "type" dans chaque dictionnaire
        # TODO: peupler self.liste avec les objets reconstruits
        pass

    def sauvegarder_json(self, chemin):
        # TODO: convertir chaque élément de self.liste en dictionnaire
        #       via sa méthode to_dict()
        # TODO: sauvegarder la liste de dictionnaires dans le fichier JSON
        #       avec une indentation de 2 et ensure_ascii=False
        pass

    def exporter_csv(self, chemin):
        # TODO: écrire un fichier CSV avec les colonnes :
        #       type, titre, genre, annee, statut
        # TODO: chaque ligne correspond à un média de self.liste
        # TODO: ne pas oublier newline="" à l'ouverture du fichier (Windows)
        pass

    def generer_rapport_txt(self, chemin):
        # TODO: compter le nombre total de médias, de films et de séries
        # TODO: regrouper les médias par statut :
        #       "à voir", "en cours", "vu"
        # TODO: écrire le rapport dans le fichier texte selon le format
        #       décrit dans l'énoncé
        pass