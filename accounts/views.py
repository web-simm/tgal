from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Password inválida')
            return redirect('login')
    else:
        return render(request, 'base.html')



def register(request):

    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Escolha outro username...')
                messages.info(request,'Escolha outro username...')
            elif User.objects.filter(email=email).exists():
                print('scolha outro email...')
                messages.info(request,'Escolha outro email...')
            else:    
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('Utilizador criado...')
                messages.info(request, 'Utilizador criado...')
                return redirect(request, 'base.html')
        else:
            print('Passwords diferentes....')
            messages.info(request, 'Passwords diferentes....')   
        return redirect('/')
    else:
        return render(request, 'geral.html')       