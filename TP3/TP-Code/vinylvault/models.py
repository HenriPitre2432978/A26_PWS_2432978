from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=150, unique=True)
    pays = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom


class Genre(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Album(models.Model):
    STATUT_CHOICES = [
        ('possede', 'Possédé'),
        ('souhait', 'Sur ma liste de souhaits'),
    ]

    titre = models.CharField(max_length=200)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name='albums')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='albums')
    annee_sortie = models.IntegerField()
    note = models.IntegerField(default=0)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='souhait')
    isFavori = models.BooleanField(default=False, verbose_name="Coup de coeur")

    image = models.ImageField(default="", upload_to='albums/', verbose_name="Image")

    def __str__(self):
        return f"{self.titre} — {self.artiste}"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    titre = models.CharField(max_length=200)
    duree = models.CharField(max_length=10, blank=True)  #X:xx 3:34
    nb = models.IntegerField(verbose_name="Numéro")

    class Meta:
        ordering = ['nb']  # trier song par le numero de tack

    def __str__(self):
        return f"{self.nb}. {self.titre}"