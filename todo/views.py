from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from rest_framework import status
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate#, login

# Create your views here.

class IndexView(APIView):
    """
    Lists out all todo tasks and POST new ones
    """

    def get(self, request, format=None):
        """
        get request lists out all tasks
        """
        tasks = Todo.objects.filter(user=request.user)  #fetching tasks of logged in user
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # creating new todo task with the POST data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetail(APIView):
    """
    Retrieve, update or delete a todo instance
    """

    def get(self, request, pk, format=None):
        task = get_object_or_404(Todo, pk=pk) # fetching the details of one particular task
        if request.user == task.user:
            serializer = TodoSerializer(task)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    
    def put(self, request, pk, format=None):
        """
        updating task with respect to the new data
        """
        task = get_object_or_404(Todo, pk=pk)
        if request.user == task.user:
            serializer = TodoSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, pk, format=None):
        """
        Deleting a particular task
        """
        task = get_object_or_404(Todo, pk=pk)
        if request.user == task.user:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)




    