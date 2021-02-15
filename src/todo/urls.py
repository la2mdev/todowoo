from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),
    path('todo_list/', views.todo_list, name='todo_list')
]
