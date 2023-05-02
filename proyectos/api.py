#Un Viewset Clase que define las operaciones que se pueden realizar en un conjunto de datos como:
#listar, crear, devolver, actualiza o borrar un objeto.
#Ademas podemos definir quien puede consultar esto yque peticiones se pueden hacer 
#y enviar autentificaciones.

from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class CrudApi(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]