from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.contato, name='contato'),
    path('adote/', views.adote, name='adote'),
    path('doação/', views.doe, name='doe'),
    path('quem-somos/', views.ben, name='ben'),
    path('enviar-email-adocao/', views.enviar_email_adocao, name='enviar_email_adocao'),
]
