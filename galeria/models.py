from django.db import models

# Create your models here.

class Galeria(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    des = models.TextField()
    price = models.IntegerField()

# Criação na db galeria "tgal" a tabela "galeria_galeria"

# python manage.py makemigrations

# python manage.py sqlmigrate galeria 0001

# -- Create model Galeria
# --
# CREATE TABLE "galeria_galeria" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "img" varchar(100) NOT NULL, "des" text NOT NULL, "price" integer NOT NULL);
# COMMIT;

# python manage.py migrate     

