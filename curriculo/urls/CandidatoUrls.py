from django.urls import path
from curriculo.views.CandidatoView import *
urlpatterns = [
    path("enviar-curriculo", inserir_curriculo, name='enviar-curriculo')
]