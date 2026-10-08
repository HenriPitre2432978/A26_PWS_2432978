from django.contrib import admin
from .models import Artiste, Genre, Album, Song

#store coté admin pour pouvoir handle tout admin side
admin.site.register(Artiste)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)

#Remplissage données de base:
#https://share.google/aimode/3gcg7xHODMq88ndyQ
