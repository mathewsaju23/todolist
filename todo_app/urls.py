from django.urls import path
from .views import TodolistView, TodoitemView

urlpatterns = [
    path('list/', TodolistView.as_view()),
    path('list/<int:pk>', TodoitemView.as_view()),

]
