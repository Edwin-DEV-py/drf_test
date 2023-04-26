from django.db import models

class Proyectos(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
