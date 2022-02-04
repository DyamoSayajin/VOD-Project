from django.shortcuts import render

titre = {
        'titre':'Site-VOD',
        'soustitres':'Hello-World',
        'videos' : 
        [
            {
                'titre':'Eternals',
                'description':'Marvel',
            
            },
            {
                'titre':'StarWars',
                'description':'LucasFilm'

            },
            {
                'titre':'RioLion',
                'description':'Disney'
            }
        ]
}

def acceuil(request):
    return render (request,'index.html',titre)

def player(request):
    return render (request,'player.html')

# Create your views here.
