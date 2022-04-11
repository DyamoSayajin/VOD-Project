import os
import cv2
from VOD.api_tmdb import infos_films

def liste_videos():
    liste = []
    liste_fichier= os.listdir("d:/Users/Noa/Documents/GitHub/VOD-Project/ServeurVOD/Videos")
    for fichier in liste_fichier:
        file_path = os.path.join("d:/Users/Noa/Documents/GitHub/VOD-Project/ServeurVOD/Videos/",fichier)
        vid = cv2.VideoCapture(file_path)
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        nom_video = ''.join(fichier.split('.')[:-1]) #Séparation de l'extension et du nom.
        recherche_tmdb = infos_films(nom_video)
        dictionnaire = {
            'nom':recherche_tmdb['titre'],
            'fichier':fichier,
            'hauteur':height,
            'largeur':width,
            'lien':file_path,
            'description':recherche_tmdb['description'],
            'poster':'https://image.tmdb.org/t/p/w500/{}'.format(recherche_tmdb['poster'])
        }
        liste.append(dictionnaire)
    return liste

liste_videos()