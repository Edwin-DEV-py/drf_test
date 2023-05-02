#transforma los objectos de Django, como los modelos, en formatos que puedan trasmitirse
#o almacenar en otro lugar, se pueden convertir en JSON o XML para enviar la informacion
#a traves de una API

#peticiones GET, POST, PUT, DELETE

from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id','create_date')
        

