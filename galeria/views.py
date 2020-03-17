from django.shortcuts import render
from .models import Galeria

# Create your views here.

def galeria(request):

    dest1 = Galeria()
    dest1.name = 'Sol'
    dest1.des = 'O brilho que faz...'
    dest1.img = ''
    dest1.price = 25



    return render(request, 'geral.html', {'dest1': dest1})