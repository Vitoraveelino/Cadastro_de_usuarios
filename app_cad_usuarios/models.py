from django.db import models

class usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.AutoField(max_length=255)
    idade = models.IntegerField()