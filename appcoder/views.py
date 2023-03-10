from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import curso

# Create your views here.
def Curso(request, camada):
    Curso = curso(nombre='desarollo web', camada=camada)
    Curso.save()
    documento_de_texto = f'--->Curso: {Curso.nombre}, camada: {Curso.camada}'

    return HttpResponse(documento_de_texto)