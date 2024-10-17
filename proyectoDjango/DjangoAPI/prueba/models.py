from django.db import models

# Create your models here.

class generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=30)

    class Meta:
        db_table = "generos"

class usuarios (models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    fk_generos = models.ForeignKey(generos, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = "usuarios"