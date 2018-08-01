from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from rest_framework import status
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class IndexView(APIView):
    """
    Lists out all todo tasks
    """

    def get(self, request, format=None):
        """
        get request lists out all tasks
        """
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetail(APIView):
    """
    Retrieve, update or delete a todo instance
    """

    def get(self, request, pk, format=None):
        task = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(task)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        task = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        task = get_object_or_404(Todo, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

