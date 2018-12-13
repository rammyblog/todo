from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addTodo, name = 'addTodo'),
    path('complete/<todo_id>', views.completeTodo, name = 'complete'),
     path('deletecomplete', views.deleteCompleted, name = 'deletecomplete'),
     path('deleteall', views.deleteAll, name = 'deleteall'),
]