from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario=models.CharField(max_length=20)
    email_usuario=models.EmailField()

    def __str__(self) :
        return self.nombre_usuario
