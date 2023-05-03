#Un Viewset Clase que define las operaciones que se pueden realizar en un conjunto de datos como:
#listar, crear, devolver, actualiza o borrar un objeto.
#Ademas podemos definir quien puede consultar esto yque peticiones se pueden hacer 
#y enviar autentificaciones.
from django.http import HttpResponse ##prueba

from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

response = HttpResponse() ##prueba
response['Access-Control-Allow-Origin'] = 'http://localhost:5173' ##prueba


class CrudApi(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    
    ##prueba listar
    def list(self, request, *args, **kwargs):
        response = super(CrudApi, self).list(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        return response
    
    ##prueba update
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
