from typing import Generic
from django.shortcuts import render
from rest_framework import views
from .serializers import TodoitemSerializer, TodolistSerializer
from .models import Todoitem, Todolist
from django.views.generic import ListView
from rest_framework import generics

# Create your views here.


class TodolistView(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer


class TodoitemView(generics.ListCreateAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoitemSerializer
