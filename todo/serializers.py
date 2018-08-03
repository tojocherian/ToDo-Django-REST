from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Model serializer of Todo class
    """
    class Meta:
        model = Todo
        fields = ('id','user','text','completed','timestamp')
