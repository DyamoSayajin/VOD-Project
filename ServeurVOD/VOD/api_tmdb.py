import requests
api_key = '5e96cf0ae8c74ed024765f33ef79438d'

def infos_films(titre):

    reponse = requests.get('https://api.themoviedb.org/3/search/movie?api_key={}&language=fr-FR&page=1&query={}'.format(api_key,titre))
    film = reponse.json()['results'][0]
    resultat = {
        'titre':film['title'],
        'poster':film['poster_path'],
        'description':film['overview']
    }
    return resultat
