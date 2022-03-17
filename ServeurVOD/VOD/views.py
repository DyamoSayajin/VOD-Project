from django.shortcuts import render
from VOD.dico_video import liste_videos


#Dictionnaire contenant le titre et la description de chaque fichier dans le dossier vidéos.Elle sera renvoyé par une fonction dans un autre fichier python.
titre = {
    'titre':'BONJOUR',
    'soustitres':'COMME CA VA VA ?',
    'videos': liste_videos()
}

def acceuil(request):    #Retourne la page html de base. La fonction prend en argument le dictionnaire pour que la page html affiche la liste des vidéos disponibles.
    return render (request,'index.html',titre)

def player(request):     #Retourne la page player avec la vidéo choisie. 
    nom_film = request.GET.get("name")
    return render (request,'player.html',{'nom_film' : nom_film})

# Create your views here.
