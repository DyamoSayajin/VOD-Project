import os
import cv2


def liste_videos():
    liste = []
    liste_fichier= os.listdir("d:/Users/Noa/Documents/GitHub/VOD-Project/ServeurVOD/Videos") #Liste des fichiers présent, avec extensions.
    for fichier in liste_fichier:
        file_path = os.path.join("d:/Users/Noa/Documents/GitHub/VOD-Project/ServeurVOD/Videos/",fichier)
        vid = cv2.VideoCapture(file_path)
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        nom_video = ''.join(fichier.split('.')[:-1]) #Séparation de l'extension et du nom.
        dictionnaire = {
            'nom':nom_video,
            'hauteur':height,
            'largeur':width
        }
        liste.append(dictionnaire)
    return liste
