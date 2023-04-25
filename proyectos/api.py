#Un Viewset Clase que define las operaciones que se pueden realizar en un conjunto de datos como:
#listar, crear, devolver, actualiza o borrar un objeto.
#Ademas podemos definir quien puede consultar esto yque peticiones se pueden hacer 
#y enviar autentificaciones.

from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class Proyecto_ViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all() #conjunto de datos
    permission_classes = [permissions.AllowAny] #otorgar permisos a la aplicacion cliente
    serializer_class = Proyecto_serializer #especificar el serializer