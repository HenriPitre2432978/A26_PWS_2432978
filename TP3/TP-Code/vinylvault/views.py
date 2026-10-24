from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Album, Artiste, Song
from .forms import ArtisteForm, AlbumForm, SongForm

#GOTO Methods
def accueil(request):
    return render(request, 'vinylvault/accueil.html')

def a_propos(request):
    return render(request, 'vinylvault/a_propos.html')

def liste_albums(request):
    albums = Album.objects.all()
    return render(request, 'vinylvault/liste_albums.html', {'albums': albums})

def detail_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'vinylvault/detail_album.html', {'album': album})

def liste_artistes(request):
    artistes = Artiste.objects.all()
    return render(request, 'vinylvault/liste_artistes.html', {'artistes': artistes})

#=========================== Artiste
def ajouter_artiste(request):
    if request.method == 'POST':
        form = ArtisteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'artiste a été ajouté avec succès.")
            return redirect('vinylvault:liste_artistes')
        else:
            messages.error(request, "Le formulaire contient des erreurs, vérifiez les champs.")
    else:
        form = ArtisteForm()
    return render(request, 'vinylvault/artiste_form.html', {'form': form, 'titre': 'Ajouter un artiste'})


def modifier_artiste(request, pk):
    artiste = get_object_or_404(Artiste, pk=pk)
    if request.method != 'POST':
        form = ArtisteForm(instance=artiste)
        return render(request, 'vinylvault/artiste_form.html', {'form': form, 'titre': "Modifier l'artiste"})

    form = ArtisteForm(request.POST, instance=artiste)
    if not form.is_valid():
        messages.error(request, "Le formulaire contient des erreurs, vérifiez les champs.")
        return render(request, 'vinylvault/artiste_form.html', {'form': form, 'titre': "Modifier l'artiste"})

    form.save()
    messages.success(request, "L'artiste a été modifié avec succès.")
    return redirect('vinylvault:liste_artistes')


def supprimer_artiste(request, pk):
    artiste = get_object_or_404(Artiste, pk=pk)
    if request.method == 'POST':
        nom = artiste.nom
        artiste.delete()
        messages.success(request, f"L'artiste « {nom} » a été supprimé.")
        return redirect('vinylvault:liste_artistes')
    return render(request, 'vinylvault/artiste_confirm_delete.html', {'artiste': artiste})


#=========================== Album

def ajouter_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'album a été ajouté avec succès.")
            return redirect('vinylvault:liste_albums')
        else:
            messages.error(request, "Le formulaire contient des erreurs, vérifiez les champs.")
    else:
        form = AlbumForm()
    return render(request, 'vinylvault/album_form.html', {'form': form, 'titre': 'Ajouter un album'})


def modifier_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, "L'album a été modifié avec succès.")
            return redirect('vinylvault:detail_album', pk=album.pk)
        else:
            messages.error(request, "Le formulaire contient des erreurs, vérifiez les champs.")
    else:
        form = AlbumForm(instance=album)
    return render(request, 'vinylvault/album_form.html', {'form': form, 'titre': "Modifier l'album"})


def supprimer_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        titre = album.titre
        album.delete()
        messages.success(request, f"L'album « {titre} » a été supprimé.")
        return redirect('vinylvault:liste_albums')
    return render(request, 'vinylvault/album_confirm_delete.html', {'album': album})

#=========================== chanson

def ajouter_chanson(request, album_pk):
    # album_pk vient direct de l'URL, pas besoin de le faire choisir dans le formulaire
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = SongForm(request.POST, album=album)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            messages.success(request, "La chanson a été ajoutée avec succès.")
            return redirect('vinylvault:detail_album', pk=album.pk)
        else:
            messages.error(request, "Le formulaire contient des erreurs, vérifiez les champs.")
    else:
        form = SongForm(album=album)
    return render(request, 'vinylvault/song_form.html', {'form': form, 'album': album})
