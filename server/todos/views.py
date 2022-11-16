from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TodoSerializer
from .models import Todo

from django.contrib.auth.decorators import login_required


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(Todo, pk=todo_pk)
        if request.method == 'PUT':
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            todo.delete()
            return Response({ 'id': todo_pk }, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
