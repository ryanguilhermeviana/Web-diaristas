from django.urls import path
from .views import diaristas_localidade_view, endereco_cep_view


urlpatterns = [
    path('diaristas/localidades', 
         diaristas_localidade_view.DiaristasLocalidades.as_view(), 
         name='diaristas-localidades-list'),

    path('enderecos',
         endereco_cep_view.EnderecoCep.as_view(), 
         name='endereco-cep-list')
]
