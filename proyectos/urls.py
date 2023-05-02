#Con los routes definimos las urls que corresponden a las vistas de la API
#por ejemplo el objeto router genera automaticamente las urls para listar un objeto, o 
#ver un objecto especifico (pk)

from rest_framework import routers
from .api import *

Router =  routers.DefaultRouter()
Router.register('api/proyectos', CrudApi, 'proyectos') #ruta con los tipicos crud

#exportamos par agenerar urls en este caso POST GET PUT DELETE
urlpatterns = Router.urls
