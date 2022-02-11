import os

def liste_videos():
    liste_fichier= os.listdir(r'D:\Users\Noa\Documents\GitHub\VOD-Project\ServeurVOD\Videos') #Liste des fichiers présent, avec extensions.
    liste_nom = []
    for fichier in liste_fichier:
        nom_video = ''.join(fichier.split('.')[:-1]) #Séparation de l'extension et du nom.
        liste_nom.append(nom_video)   #Ajout du nom sans l'extension à la nouvelle liste.
    return liste_nom

print(liste_videos())
    
"""import cv2
file_path = "./video.avi"
vid = cv2.VideoCapture(file_path)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
"""