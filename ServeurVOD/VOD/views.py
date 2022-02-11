from django.shortcuts import render


#Dictionnaire contenant le titre et la description de chaque fichier dans le dossier vidéos.Elle sera renvoyé par une fonction dans un autre fichier python.
titre = {}

def acceuil(request):    #Retourne la page html de base. La fonction prend en argument le dictionnaire pour que la page html affiche la liste des vidéos disponibles.
    return render (request,'index.html',titre)

def player(request):     #Retourne la page player avec la vidéo choisie. 
    return render (request,'player.html')

# Create your views here.
