#CREATION DE DONNÉES DE LA DATABASE RÉALISÉE ENTIÈREMENT AVEC L'IA,
#J'AI DÛ LA REFAIRE APRÈS UN PROBLÈME DE MIGRATIONS SUR MA DATABASE
#https://chatgpt.com/s/t_6ac7e3dc7a508191846adfe4bf63e361

import os
import django

# 1. Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# 2. Initialize Django
django.setup()

# 3. Import models after Django has been initialized
from vinylvault.models import Artiste, Genre, Album, Song


def run():
    print("🌱 Seeding database...")

    # --------------------------------------------------
    # Genres
    # --------------------------------------------------
    genres_data = [
        "Rock",
        "Pop",
        "Hip-Hop",
        "Jazz",
        "Électronique",
        "Classique",
        "Metal",
        "R&B",
    ]

    genres = {}

    for nom in genres_data:
        genre, _ = Genre.objects.get_or_create(nom=nom)
        genres[nom] = genre

    # --------------------------------------------------
    # Artistes
    # --------------------------------------------------
    artistes_data = [
        {
            "nom": "Daft Punk",
            "pays": "France",
        },
        {
            "nom": "The Beatles",
            "pays": "Royaume-Uni",
        },
        {
            "nom": "David Bowie",
            "pays": "Royaume-Uni",
        },
        {
            "nom": "Nirvana",
            "pays": "États-Unis",
        },
        {
            "nom": "Michael Jackson",
            "pays": "États-Unis",
        },
        {
            "nom": "Stromae",
            "pays": "Belgique",
        },
        {
            "nom": "Radiohead",
            "pays": "Royaume-Uni",
        },
        {
            "nom": "Metallica",
            "pays": "États-Unis",
        },
    ]

    artistes = {}

    for data in artistes_data:
        artiste, _ = Artiste.objects.get_or_create(
            nom=data["nom"],
            defaults={"pays": data["pays"]},
        )
        artistes[data["nom"]] = artiste

    # --------------------------------------------------
    # Albums
    # --------------------------------------------------
    albums_data = [
        {
            "titre": "Random Access Memories",
            "artiste": "Daft Punk",
            "genre": "Électronique",
            "annee_sortie": 2013,
            "note": 5,
            "statut": "possede",
            "isFavori": True,
            "songs": [
                ("Give Life Back to Music", "4:34", 1),
                ("Get Lucky", "6:09", 2),
                ("Instant Crush", "5:37", 3),
                ("Lose Yourself to Dance", "5:53", 4),
                ("Touch", "8:18", 5),
            ],
        },
        {
            "titre": "Abbey Road",
            "artiste": "The Beatles",
            "genre": "Rock",
            "annee_sortie": 1969,
            "note": 5,
            "statut": "possede",
            "isFavori": True,
            "songs": [
                ("Come Together", "4:20", 1),
                ("Something", "3:03", 2),
                ("Maxwell's Silver Hammer", "3:27", 3),
                ("Oh! Darling", "3:27", 4),
                ("Here Comes the Sun", "3:05", 5),
                ("Because", "2:45", 6),
            ],
        },
        {
            "titre": "The Rise and Fall of Ziggy Stardust",
            "artiste": "David Bowie",
            "genre": "Rock",
            "annee_sortie": 1972,
            "note": 5,
            "statut": "possede",
            "isFavori": False,
            "songs": [
                ("Five Years", "4:43", 1),
                ("Soul Love", "3:33", 2),
                ("Starman", "4:16", 3),
                ("Lady Stardust", "3:20", 4),
                ("Ziggy Stardust", "3:13", 5),
            ],
        },
        {
            "titre": "Nevermind",
            "artiste": "Nirvana",
            "genre": "Rock",
            "annee_sortie": 1991,
            "note": 4,
            "statut": "possede",
            "isFavori": True,
            "songs": [
                ("Smells Like Teen Spirit", "5:01", 1),
                ("In Bloom", "4:15", 2),
                ("Come as You Are", "3:39", 3),
                ("Lithium", "4:17", 4),
                ("Polly", "2:57", 5),
            ],
        },
        {
            "titre": "Thriller",
            "artiste": "Michael Jackson",
            "genre": "Pop",
            "annee_sortie": 1982,
            "note": 5,
            "statut": "possede",
            "isFavori": True,
            "songs": [
                ("Wanna Be Startin' Somethin'", "6:03", 1),
                ("Baby Be Mine", "4:20", 2),
                ("The Girl Is Mine", "3:42", 3),
                ("Thriller", "5:57", 4),
                ("Beat It", "4:18", 5),
                ("Billie Jean", "4:54", 6),
            ],
        },
        {
            "titre": "Racine carrée",
            "artiste": "Stromae",
            "genre": "Pop",
            "annee_sortie": 2013,
            "note": 4,
            "statut": "possede",
            "isFavori": False,
            "songs": [
                ("Ta fête", "2:56", 1),
                ("Papaoutai", "3:52", 2),
                ("Formidable", "3:34", 3),
                ("Tous les mêmes", "3:59", 4),
                ("Carmen", "3:09", 5),
            ],
        },
        {
            "titre": "OK Computer",
            "artiste": "Radiohead",
            "genre": "Rock",
            "annee_sortie": 1997,
            "note": 5,
            "statut": "souhait",
            "isFavori": False,
            "songs": [
                ("Airbag", "4:44", 1),
                ("Paranoid Android", "6:23", 2),
                ("Subterranean Homesick Alien", "4:27", 3),
                ("Karma Police", "4:21", 4),
                ("No Surprises", "3:49", 5),
            ],
        },
        {
            "titre": "Master of Puppets",
            "artiste": "Metallica",
            "genre": "Metal",
            "annee_sortie": 1986,
            "note": 4,
            "statut": "souhait",
            "isFavori": False,
            "songs": [
                ("Battery", "5:12", 1),
                ("Master of Puppets", "8:36", 2),
                ("The Thing That Should Not Be", "6:37", 3),
                ("Welcome Home (Sanitarium)", "6:27", 4),
                ("Disposable Heroes", "8:16", 5),
            ],
        },
    ]

    # --------------------------------------------------
    # Create albums + songs
    # --------------------------------------------------
    for album_data in albums_data:
        artiste = artistes[album_data["artiste"]]
        genre = genres[album_data["genre"]]

        album, created = Album.objects.get_or_create(
            titre=album_data["titre"],
            artiste=artiste,
            defaults={
                "genre": genre,
                "annee_sortie": album_data["annee_sortie"],
                "note": album_data["note"],
                "statut": album_data["statut"],
                "isFavori": album_data["isFavori"],
            },
        )

        if created:
            print(f"  ✓ Album créé : {album.titre}")
        else:
            print(f"  → Album déjà présent : {album.titre}")

        # Create songs
        for titre, duree, nb in album_data["songs"]:
            Song.objects.get_or_create(
                album=album,
                nb=nb,
                defaults={
                    "titre": titre,
                    "duree": duree,
                },
            )

    print()
    print("✅ Seeding terminé !")
    print()
    print(f"Genres   : {Genre.objects.count()}")
    print(f"Artistes : {Artiste.objects.count()}")
    print(f"Albums   : {Album.objects.count()}")
    print(f"Chansons : {Song.objects.count()}")


if __name__ == "__main__":
    run()