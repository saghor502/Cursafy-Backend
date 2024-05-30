from django.shortcuts import render
from django.http import HttpResponse
from . import IA

def test(request):
    return HttpResponse("Hello, world.")


def paises(request):
    return HttpResponse(["Mexico", "USA"])


def estados(request):
    return HttpResponse(["Chihuahua", "Coahuila"])


def competencias(request):
    return HttpResponse(["Matematicas", "Español"])


def usuarios(request):
    return HttpResponse()


def usuariosMexicanos(request):
    return HttpResponse()
