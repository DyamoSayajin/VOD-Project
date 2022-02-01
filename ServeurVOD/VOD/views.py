from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def acceuil(request):
    return HttpResponse("<h1>Projet-VOD</h1>")

def player(request):
    return HttpResponse("<h1>Page player d'une vidéo</h1>")

# Create your views here.
