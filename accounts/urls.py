from django.urls import path
from . import views
from galeria.models import Galeria

urlpatterns = [
    path("geral", views.register, name="register"),
    path("geral", views.login, name="login")
]