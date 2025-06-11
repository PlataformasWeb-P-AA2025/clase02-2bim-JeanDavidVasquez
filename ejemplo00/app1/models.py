from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s - edad: %d" % (self.nombre, self.apellido, self.cedula, self.edad)
    
class ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    poblacion = models.IntegerField()
    def __str__(self):
        return "%s - poblacion: %d" % (self.nombre, self.poblacion)

