# media.py


class Media:
    """Classe de base représentant un média (film ou série)."""

    def __init__(self, titre, genre, annee, statut):
        # TODO: initialiser les attributs titre, genre, annee, statut
        pass

    def __str__(self):
        # TODO: retourner une chaîne lisible au format :
        # [statut] Titre (annee) — genre
        pass

    def to_dict(self):
        # TODO: retourner un dictionnaire avec tous les attributs de l'instance
        # Ne pas oublier la clé "type" avec la valeur "Media"
        pass


class Film(Media):
    """Représente un film. Hérite de Media."""

    def __init__(self, titre, genre, annee, statut, duree):
        # TODO: appeler le constructeur parent avec super()
        # TODO: initialiser l'attribut duree
        pass

    def __str__(self):
        # TODO: retourner une chaîne lisible au format :
        # [statut] Titre (annee) — genre — duree min
        pass

    def to_dict(self):
        # TODO: appeler super().to_dict() pour obtenir le dictionnaire de base
        # TODO: ajouter les clés spécifiques à Film (type, duree)
        # TODO: retourner le dictionnaire complet
        pass


class Serie(Media):
    """Représente une série. Hérite de Media."""

    def __init__(self, titre, genre, annee, statut, nb_saisons, nb_episodes):
        # TODO: appeler le constructeur parent avec super()
        # TODO: initialiser les attributs nb_saisons et nb_episodes
        pass

    def __str__(self):
        # TODO: retourner une chaîne lisible au format :
        # [statut] Titre (annee) — genre — nb_saisons saisons, nb_episodes épisodes
        pass

    def to_dict(self):
        # TODO: appeler super().to_dict() pour obtenir le dictionnaire de base
        # TODO: ajouter les clés spécifiques à Serie (type, nb_saisons, nb_episodes)
        # TODO: retourner le dictionnaire complet
        pass