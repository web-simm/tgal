from django.urls import path
from . import views
from .models import Galeria

urlpatterns = [
    path('',views.galeria, name='geral'),
]