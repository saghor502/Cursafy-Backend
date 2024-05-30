from django.urls import path

from . import views

urlpatterns = [
    path("test", views.test, name="index"),
    path("paises", views.paises, name="paises"),
    path("estados", views.estados, name="estados"),
    path("competencias", views.competencias, name="competencias"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("usuariosMexicanos", views.usuariosMexicanos, name="usuariosMexicanos"),
]
