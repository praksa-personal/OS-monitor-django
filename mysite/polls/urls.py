from django.urls import path
from . import views

urlpatterns = [
    path('', views.allData, name='getAll'),
    path('cpu', views.cpu, name='cpu'),
    path('memory', views.memory, name='memory'),
    path('table', views.table, name='table'),
]
