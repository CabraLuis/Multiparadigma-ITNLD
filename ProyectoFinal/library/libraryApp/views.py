from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hola soy homero omero chino")