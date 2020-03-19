from django.shortcuts import render
from .models import Galeria

# Create your views here.

def galeria(request):

    dests = Galeria.objects.all()

    
    return render(request, 'geral.html', {'dests': dests})