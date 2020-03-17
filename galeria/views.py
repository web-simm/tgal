from django.shortcuts import render
from .models import Galeria

# Create your views here.

def galeria(request):

    dest1 = Galeria()
    dest1.name = 'Sol'
    dest1.des = 'O brilho que faz...'
    dest1.img = '814.jpg'
    dest1.price = 25

    dest2 = Galeria()
    dest2.name = 'Lua'
    dest2.des = 'O brilho que faz...'
    dest2.img = '/static/815.jpg'
    dest2.price = 25

    dest3 = Galeria()
    dest3.name = 'Chuva'
    dest3.des = 'O brilho que faz...'
    dest3.img = '816.jpg'
    dest3.price = 25

    dests = [dest1, dest2, dest3]

    return render(request, 'geral.html', {'dests': dests})